# INDIVIDUAL STOCK CHATGPT PACKET - 5608 四維航

## Metadata
- generated_at: 2026-07-08 22:27:51 Asia/Taipei
- stock_id: 5608
- stock_name: 四維航
- packet_status: standard_180d_window_packet
- latest_price_date: 20260708
- price_rows: 300
- latest_tdcc_date: 20260703
- tdcc_rows: 10
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/5608_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/5608_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5608_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5608_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5608_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5608_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/5608_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/5608_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5608_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5608_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/5608_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/5608_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/5608.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/5608.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/5608.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/5608.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/5608_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/5608_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/5608_latest.md?ref=main

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
- model_category_display_zh: 區間內轉強 / 挑戰前高觀察
- score_interpretation_zh: 模型分數中上，代表條件有支持，但仍需依風控管理。 目前允許依部位規則建立第一筆，後續用風控與追蹤項目管理。
- action_summary_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。
- entry_strategy_zh: 回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：回測 23EMA 附近；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

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
- date: 20260708
- open: 14.7
- high: 14.9
- low: 14.45
- close: 14.75
- volume: 1370018
- ma5: 14.65
- ema23_primary: 14.65
- distance_to_ema23_pct: 0.7
- ma20: 14.66
- ma60: 14.95
- ma120: 16.14
- return_5d: 3.51
- return_20d: -1.99
- volume_ratio: 1.04
- distance_to_ma20_pct_auxiliary: 0.58
- distance_to_high_60_pct: -12.72

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260610,15.1,15.1,14.8,14.8,1199565,14.85,-0.34,14.58,15.57,0.66
20260611,14.8,14.9,14.55,14.9,1062464,14.85,0.31,14.6,15.53,0.6
20260612,14.9,15.4,14.9,15.1,1979718,14.87,1.51,14.64,15.5,1.11
20260615,15.4,15.55,15.05,15.1,1238006,14.89,1.39,14.69,15.46,0.69
20260616,15.4,15.4,14.85,14.9,1117043,14.89,0.04,14.72,15.42,0.62
20260617,15,15.25,14.75,15.1,1150917,14.91,1.27,14.77,15.39,0.64
20260618,15.15,15.2,14.9,14.9,924075,14.91,-0.07,14.79,15.36,0.51
20260622,14.95,15,14.7,14.8,1672344,14.9,-0.68,14.82,15.33,0.93
20260623,14.8,14.85,14.6,14.6,1237699,14.88,-1.86,14.82,15.29,0.72
20260624,14.6,14.75,14.5,14.5,887761,14.84,-2.32,14.81,15.26,0.54
20260625,14.65,14.75,14.5,14.6,724629,14.82,-1.51,14.82,15.23,0.45
20260626,14.5,14.65,14.1,14.1,1711744,14.76,-4.5,14.81,15.19,1.05
20260629,14.3,14.3,14.1,14.15,857735,14.71,-3.83,14.8,15.16,0.53
20260630,14.2,14.3,14.15,14.25,1101000,14.67,-2.89,14.77,15.12,0.75
20260701,14.3,14.4,14.15,14.25,985000,14.64,-2.66,14.74,15.09,0.7
20260702,14.25,14.4,14.15,14.25,976000,14.61,-2.44,14.7,15.05,0.75
20260703,14.25,14.9,14.25,14.8,2665135,14.62,1.21,14.69,15.02,1.96
20260706,14.95,15.4,14.9,14.95,1888000,14.65,2.05,14.69,15,1.44
20260707,15.05,15.1,14.4,14.5,1485799,14.64,-0.94,14.68,14.97,1.13
20260708,14.7,14.9,14.45,14.75,1370018,14.65,0.7,14.66,14.95,1.04
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 28.91
- over_600_ratio: 26.29
- over_800_ratio: 25.41
- over_1000_ratio: 23.6
- over_400_change_1w: 0.12
- over_800_change_1w: 0.13
- over_1000_change_1w: -0.08
- tdcc_consecutive_up_weeks: 9
- all_thresholds_up: False
- high_thresholds_up: True

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,27.52,,24.33,,23.2,,0,False,False
20260508,28.06,0.54,24.64,0.31,23.28,0.08,1,True,True
20260515,28.07,0.01,24.82,0.18,23.69,0.41,2,True,True
20260522,28.26,0.19,24.78,-0.04,23.43,-0.26,3,False,False
20260529,28.32,0.06,24.63,-0.15,23.28,-0.15,4,False,False
20260605,28.56,0.24,24.64,0.01,23.51,0.23,5,False,True
20260612,28.75,0.19,25.06,0.42,23.72,0.21,6,True,True
20260618,28.77,0.02,25.14,0.08,23.8,0.08,7,True,True
20260626,28.79,0.02,25.28,0.14,23.68,-0.12,8,False,True
20260703,28.91,0.12,25.41,0.13,23.6,-0.08,9,False,True
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 5608 | 四維航 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | repeated_but_no_breakout | 1.事實發生日:115/07/06 2.接受資金貸與之: (1)公司名稱:四維航業股份有限公司 (2)與資金貸與他人公司之關係: 四維為 DONG LIEN 之母公司 (3)資金貸與之限額(仟元):13,283,095 (4)原資金貸與之餘額(仟元):1,703,975 (5)本次新增資金貸與之金額(仟元):867,598 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):2,571,573 (8)本次新增資金貸與之原因: 償還借款及營業週轉 (1)公司名稱:VALOR PESCADORES S.A. PANAMA (2)與資金貸與他人公司之關係: VALOR PESCADORES S.A. PANAMA為 DONG LIEN 之子公司 (3)資金貸與之限額(仟元):13,283,095 (4)原資金貸與之餘額(仟元):238,875 (5)本次新增資金貸與之金額(仟元):607,668 (6)是否為董事會授權董事長對同一貸與對象分次撥貸或循環動用之資金貸與:是 (7)迄事實發生日止資金貸與餘額(仟元):846,543 (8)本次新增資金貸與之原因: 購置船舶設備 3.接受資金貸與公司所提供擔保品之: (1)內容: 無 (2)價值(仟元):0 4.接受資金貸與公司最近期財務報表之: (1)資本(仟元):4,046,337 (2)累積盈虧金額(仟元):2,166,490 5.計息方式: 無息借款 6.還款之: (1)條件: 不適用 (2)日期: 一年內到期還款 7.迄事實發生日為止，資金貸與餘額(仟元): 4,954,670 8.迄事實發生日為止，資金貸與餘額占公開發行公司最近期財務報表淨值之比率: 51.20 9.公司貸與他人資金之來源: 子公司本身 10.其他應敘明事項: (1)上述資金貸與四維及VALOR總金額為美金107,000,000元，依匯率＠31.945換算    新台幣公告之。  (2)本次新增第一筆資金貸與金額為美金27,000,000元，占淨值百分比為8.91%；    新增第二筆資金貸與金額為美金19,000,000元，占淨值百分比為6.27%。  (3)DONG LIEN MARITIME S.A. PANAMA 資金貸與他人明細如下:                                                                                                            單位:新台幣仟元    接受資金貸與之公司名稱      財務報表資本       財務報表累積盈虧金額   --------------------      -----------       ------------------   四維                        3,892,761                2,017,952   VALOR                         153,576                  148,538   ====================      ===========       ==================         合 計                 4,046,337                2,166,490   ====================      ===========       ==================；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260708 | 5608 | 四維航 | 1 | 1 | 3 | 3 | 9 | repeated_but_no_breakout | 近 10 日上榜 3 次、近 20 日上榜 9 次，但尚未有效突破，需等待攻擊確認。 |

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
