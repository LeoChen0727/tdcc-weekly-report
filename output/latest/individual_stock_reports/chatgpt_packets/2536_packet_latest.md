# INDIVIDUAL STOCK CHATGPT PACKET - 2536 宏普

## Metadata
- generated_at: 2026-07-10 22:26:56 Asia/Taipei
- stock_id: 2536
- stock_name: 宏普
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
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/2536_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/2536_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2536_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2536_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2536_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2536_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/2536_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/2536_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2536_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2536_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/2536_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/2536_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/2536.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/2536.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/2536.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/2536.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/2536_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/2536_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/2536_latest.md?ref=main

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
- date: 20260709
- open: 19.3
- high: 19.65
- low: 19.2
- close: 19.55
- volume: 1355882
- ma5: 20.16
- ema23_primary: 20.7
- distance_to_ema23_pct: -5.56
- ma20: 21.08
- ma60: 20.86
- ma120: 21.95
- return_5d: -7.78
- return_20d: -9.49
- volume_ratio: 1.01
- distance_to_ma20_pct_auxiliary: -7.27
- distance_to_high_60_pct: -13.11

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260611,21.85,21.9,21.25,21.65,847408,20.52,5.53,20.13,21.28,1.56
20260612,21.9,22.15,21.6,21.95,1470877,20.63,6.37,20.23,21.27,2.49
20260615,22.1,22.1,21.55,21.7,796531,20.72,4.71,20.3,21.25,1.28
20260616,21.7,21.75,21.35,21.4,478923,20.78,2.98,20.37,21.23,0.75
20260617,21.4,21.5,21.2,21.4,672295,20.83,2.73,20.43,21.21,1.03
20260618,21.75,22.45,21.6,22.35,4132953,20.96,6.64,20.55,21.22,4.92
20260622,22.35,22.35,21.25,21.3,2579265,20.99,1.49,20.62,21.2,2.72
20260623,21.65,21.65,21.2,21.25,941857,21.01,1.15,20.7,21.18,1
20260624,21.25,21.55,21.1,21.3,533945,21.03,1.27,20.79,21.16,0.56
20260625,21.45,21.5,21.2,21.25,638445,21.05,0.95,20.89,21.15,0.67
20260626,21.25,21.25,20.9,21,796751,21.05,-0.22,20.96,21.13,0.83
20260629,21.05,21.4,21.05,21.2,371633,21.06,0.67,21.05,21.11,0.39
20260630,21.2,21.25,21,21.05,828000,21.06,-0.04,21.11,21.09,0.84
20260701,21.5,21.5,20.85,20.85,912000,21.04,-0.91,21.18,21.07,0.9
20260702,20.95,21.3,20.9,21.2,896000,21.05,0.69,21.23,21.05,0.87
20260703,21.3,21.6,21.25,21.45,1621317,21.09,1.72,21.29,21.03,1.47
20260706,21.6,21.8,21.55,21.6,4383000,21.13,2.22,21.34,21.02,3.41
20260707,19.6,19.65,19.2,19.25,1728865,20.97,-8.22,21.28,20.97,1.27
20260708,19.15,19.2,18.85,18.95,832604,20.8,-8.92,21.18,20.91,0.62
20260709,19.3,19.65,19.2,19.55,1355882,20.7,-5.56,21.08,20.86,1.01
```

## Latest TDCC Snapshot
- as_of_date: 20260703
- over_400_ratio: 77.79
- over_600_ratio: 74.83
- over_800_ratio: 71.56
- over_1000_ratio: 69.12
- over_400_change_1w: -0.51
- over_800_change_1w: -0.43
- over_1000_change_1w: -0.18
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,79.49,,73.8,,70,,0,False,False
20260508,79.54,0.05,73.61,-0.19,70.05,0.05,1,False,True
20260515,79.34,-0.2,73.42,-0.19,70.39,0.34,2,False,True
20260522,79.58,0.24,73.49,0.07,70.48,0.09,3,True,True
20260529,79.45,-0.13,73.17,-0.32,70.44,-0.04,0,False,False
20260605,79.24,-0.21,73.2,0.03,70.47,0.03,1,False,True
20260612,79.39,0.15,72.87,-0.33,70.19,-0.28,2,False,False
20260618,79.24,-0.15,73.02,0.15,70.29,0.1,3,False,True
20260626,78.3,-0.94,71.99,-1.03,69.3,-0.99,0,False,False
20260703,77.79,-0.51,71.56,-0.43,69.12,-0.18,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2536 | 宏普 | revenue_pullback | 營收成長股價回檔 | 84.0 |  | C_僅觀察_營建認列型需基本面確認 |  |  |  | stale_signal | 1.董事會決議日期:115/07/08 2.買回股份目的:維護公司信用及股東權益 3.買回股份種類:普通股 4.買回股份總金額上限(元):8,715,584,228 5.預定買回之期間:115/07/09~115/09/06 6.預定買回之數量(股):6,000,000 7.買回區間價格(元):13.50~31.50，公司股價低於區間價格下限，將繼續買回 8.買回方式:自集中交易市場買回 9.預定買回股份占公司已發行股份總數之比率(%):1.80 10.申報時已持有本公司股份之累積股數(股):0 11.申報前五年內買回公司股份之情形: 無買回 12.已申報買回但未執行完畢之情形: 無 13.董事會決議買回股份之會議紀錄: 民國115年07月08日董事會通過決議，計畫依證券交易法第28條之2規定，於中華民國115年07月09日 至115年09月06日間執行買回公司股份，預定買回數量總額為6,000仟股，其買回區間價格為新台幣每 股 13.50 元至 31.50 元。 14.「上市上櫃公司買回本公司股份辦法」第十條規定之轉讓辦法: 不適用 15.「上市上櫃公司買回本公司股份辦法」第十一條規定之轉換或認股辦法: 不適用 16.董事會已考慮公司財務狀況，不影響公司資本維持之聲明: 本次買回股份總數僅佔本公司已發行股份1.80%，且買回股份所需金額上限僅佔本公司流動資產  0.51  %，茲聲明本公司董事會已考慮公司財務狀況，上述股份之買回並不影響本公司資本維持。 17.會計師或證券承銷商對買回股份價格之合理性評估意見: 依元大證券股份有限公司之評估意見，宏普建設股份有限公司本次買回公司股份訂定之價格區間，其決 策過程具合法性，價格區間之訂定及對公司財務之影響亦尚屬合理，尚無重大異常情事。 18.其他證期局所規定之事項: 無；degraded calendar context only: ex_dividend on 20260707; status=source_stale_cached; proximity=recent; model_effect_allowed=False; pdf_effect_allowed=False；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |
| 20260709 | 2536 | 宏普 | revenue_breakout_low_response | 營收爆發低反應股 | 15.0 | 26.0 | D_降級_TDCC轉弱 |  |  |  | stale_signal | 1.董事會決議日期:115/07/08 2.買回股份目的:維護公司信用及股東權益 3.買回股份種類:普通股 4.買回股份總金額上限(元):8,715,584,228 5.預定買回之期間:115/07/09~115/09/06 6.預定買回之數量(股):6,000,000 7.買回區間價格(元):13.50~31.50，公司股價低於區間價格下限，將繼續買回 8.買回方式:自集中交易市場買回 9.預定買回股份占公司已發行股份總數之比率(%):1.80 10.申報時已持有本公司股份之累積股數(股):0 11.申報前五年內買回公司股份之情形: 無買回 12.已申報買回但未執行完畢之情形: 無 13.董事會決議買回股份之會議紀錄: 民國115年07月08日董事會通過決議，計畫依證券交易法第28條之2規定，於中華民國115年07月09日 至115年09月06日間執行買回公司股份，預定買回數量總額為6,000仟股，其買回區間價格為新台幣每 股 13.50 元至 31.50 元。 14.「上市上櫃公司買回本公司股份辦法」第十條規定之轉讓辦法: 不適用 15.「上市上櫃公司買回本公司股份辦法」第十一條規定之轉換或認股辦法: 不適用 16.董事會已考慮公司財務狀況，不影響公司資本維持之聲明: 本次買回股份總數僅佔本公司已發行股份1.80%，且買回股份所需金額上限僅佔本公司流動資產  0.51  %，茲聲明本公司董事會已考慮公司財務狀況，上述股份之買回並不影響本公司資本維持。 17.會計師或證券承銷商對買回股份價格之合理性評估意見: 依元大證券股份有限公司之評估意見，宏普建設股份有限公司本次買回公司股份訂定之價格區間，其決 策過程具合法性，價格區間之訂定及對公司財務之影響亦尚屬合理，尚無重大異常情事。 18.其他證期局所規定之事項: 無；degraded calendar context only: ex_dividend on 20260707; status=source_stale_cached; proximity=recent; model_effect_allowed=False; pdf_effect_allowed=False；營收轉強但 EPS / 毛利率尚未有結構化資料確認；營建/交屋認列型，單月營收不升級為類事欣科型 |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260709 | 2536 | 宏普 | 1 | 1 | 4 | 4 | 7 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
