# INDIVIDUAL STOCK CHATGPT PACKET - 3680 家登

## Metadata
- generated_at: 2026-06-21 22:23:34 Asia/Taipei
- stock_id: 3680
- stock_name: 家登
- packet_status: standard_180d_window_packet
- latest_price_date: 20260618
- price_rows: 152
- latest_tdcc_date: 20260618
- tdcc_rows: 8
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/3680_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/3680_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3680_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3680_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3680_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3680_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/3680_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/3680_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3680_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3680_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/3680_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/3680_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/3680.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/3680.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/3680.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/3680.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/3680_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/3680_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/3680_latest.md?ref=main

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
- date: 20260618
- open: 516
- high: 555
- low: 511
- close: 542
- volume: 3475000
- ma5: 512.8
- ema23_primary: 521.84
- distance_to_ema23_pct: 3.86
- ma20: 530.12
- ma60: 494.83
- ma120: 444.47
- return_5d: 12.92
- return_20d: -0.37
- volume_ratio: 3.4
- distance_to_ma20_pct_auxiliary: 2.24
- distance_to_high_60_pct: -13

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260522,550,581,541,568,565000,530.18,7.13,546.83,452.63,0.14
20260525,590,615,580,595,601000,535.59,11.09,553.62,455.61,0.15
20260526,603,610,583,589,594000,540.04,9.07,560.62,458.38,0.16
20260527,600,601,548,557,568000,541.45,2.87,564.05,460.57,0.16
20260528,562,568,530,535,548000,540.91,-1.09,565.75,462.57,0.16
20260529,548,556,533,540,544000,540.84,-0.15,565.9,464.83,0.18
20260601,554,554,527,536,536000,540.43,-0.82,564.5,467.55,0.2
20260602,543,544,515,527,526,539.31,-2.28,561.75,469.67,0
20260603,531,552,528,539,541000,539.29,-0.05,559.65,472.05,0.25
20260604,539,552,533,537,542000,539.1,-0.39,557.25,474.93,0.27
20260605,530,530,507,520,516000,537.51,-3.26,555.25,477.32,0.3
20260608,468,504,468,501,1686000,534.46,-6.26,549.5,479.18,1.03
20260609,511,526,501,519,1467000,533.18,-2.66,545.35,481.43,0.96
20260610,512,548,495,495.5,1682000,530.04,-6.52,540.73,483.33,1.15
20260611,495.5,498.5,466.5,480,1435000,525.87,-8.72,535.73,485.02,1.06
20260612,500,510,490,503,1397000,523.96,-4,532.48,487.05,1.1
20260615,519,528,501,502,992000,522.13,-3.86,530.38,488.65,0.87
20260616,517,518,499.5,500,1055000,520.29,-3.9,529.67,490.43,1.04
20260617,500,521,488.5,517,1690000,520.01,-0.58,530.23,492.52,1.74
20260618,516,555,511,542,3475000,521.84,3.86,530.12,494.83,3.4
```

## Latest TDCC Snapshot
- as_of_date: 20260618
- over_400_ratio: 56.82
- over_600_ratio: 51.83
- over_800_ratio: 49.53
- over_1000_ratio: 43.13
- over_400_change_1w: 0.21
- over_800_change_1w: -0.15
- over_1000_change_1w: -2.02
- tdcc_consecutive_up_weeks: 1
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,55.27,,46.21,,41.45,,0,False,False
20260508,60.17,4.9,49.56,3.35,45.76,4.31,1,True,True
20260515,61.07,0.9,50.97,1.41,48.3,2.54,2,False,True
20260522,61.34,0.27,50,-0.97,48.05,-0.25,3,False,False
20260529,58.55,-2.79,49.9,-0.1,46.96,-1.09,0,False,False
20260605,58.08,-0.47,50.9,1,46.42,-0.54,1,False,True
20260612,56.61,-1.47,49.68,-1.22,45.15,-1.27,0,False,False
20260618,56.82,0.21,49.53,-0.15,43.13,-2.02,1,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3680 | 家登 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | neckline_challenge |  |  | stale_signal | 1.法律事件之當事人: 原告:美國安堤格里斯公司(Entegris.Inc.) 被告:家登精密工業股份有限公司 2.法律事件之法院名稱或處分機關:智慧財產及商業法院智慧財產法庭 3.法律事件之相關文書案號:113年度民專訴字第53號 4.事實發生日:115/06/17 5.發生原委(含爭訟標的):美國安堤格里斯公司(Entegris.Inc.)以我司未經授權製造 「300 Diffuser FOUP」前開式晶圓傳送盒，侵害其中華民國發明第I830642號發明專 利，向智慧財產及商業法院智慧財產法庭提起損害賠償等訴訟，請求我司賠償新台幣 3000萬元等。經一審法院審理後於115年5月13日判決「駁回原告之訴」，我司不侵權 。案經我司於115年6月17日收訖原告聲請上訴在案。 6.處理過程:本公司將繼續委請法律顧問「萬國法律事務所」處理本案二審程序，以維 護公司及全體股東權益。 7.對公司財務業務影響及預估影響金額:衡酌本案起訴金額及訴狀所載理由， 我司認本訴訟於財務及業務方面，均不致因本案而有重大影響。 8.因應措施及改善情形:本公司將委請法律顧問「萬國法律事務所」處理本案。 9.其他應敘明事項(若事件發生或決議之主體係屬公開發行以上公司， 本則重大訊息同時符合證券交易法施行細則第7條第2款所定對 股東權益或證券價格有重大影響之事項):無。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=within_14d |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260618 | 3680 | 家登 | 1 | 1 | 1 | 3 | 10 | stale_signal | 反覆上榜但尚未突破，且量價、TDCC 或 benchmark 未同步轉強，需確認是否鈍化。 |

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
