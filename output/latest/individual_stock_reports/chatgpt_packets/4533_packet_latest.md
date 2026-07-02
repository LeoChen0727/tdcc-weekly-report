# INDIVIDUAL STOCK CHATGPT PACKET - 4533 協易機

## Metadata
- generated_at: 2026-07-02 22:27:16 Asia/Taipei
- stock_id: 4533
- stock_name: 協易機
- packet_status: standard_180d_window_packet
- latest_price_date: 20260702
- price_rows: 161
- latest_tdcc_date: 20260626
- tdcc_rows: 9
- tdcc_history_status: tdcc_history_ready
- individual_report_md_exists: False
- sell_strategy_summary_exists: False
- notes:

## Stable Read URLs
- packet_pages_url: not_published_to_pages_use_raw_or_github_api
- packet_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/chatgpt_packets/4533_packet_latest.md
- packet_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/chatgpt_packets/4533_packet_latest.md?ref=main
- price_window_180_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4533_price_window_180_latest.csv
- price_window_180_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4533_price_window_180_latest.csv?ref=main
- price_window_180_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4533_price_window_180_latest.txt
- price_window_180_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4533_price_window_180_latest.txt?ref=main
- price_window_180_html_pages_url: not_published_to_pages_use_raw_or_github_api
- price_window_180_html_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/price_windows/4533_price_window_180_latest.html
- price_window_180_html_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/price_windows/4533_price_window_180_latest.html?ref=main
- tdcc_window_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4533_tdcc_window_latest.csv
- tdcc_window_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4533_tdcc_window_latest.csv?ref=main
- tdcc_window_txt_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_window_txt_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/tdcc_windows/4533_tdcc_window_latest.txt
- tdcc_window_txt_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/tdcc_windows/4533_tdcc_window_latest.txt?ref=main
- price_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/stock_price_history/4533.csv
- price_pages_url: not_published_to_pages_use_raw_or_github_api
- price_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/stock_price_history/4533.csv?ref=main
- tdcc_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data/tdcc_stock_history/4533.csv
- tdcc_pages_url: not_published_to_pages_use_raw_or_github_api
- tdcc_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/data/tdcc_stock_history/4533.csv?ref=main
- individual_report_md_raw_url: https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/individual_stock_reports/4533_latest.md
- individual_report_md_pages_url: https://LeoChen0727.github.io/tdcc-weekly-report/latest/individual_stock_reports/4533_latest.md
- individual_report_md_github_api_url: https://api.github.com/repos/LeoChen0727/tdcc-weekly-report/contents/output/latest/individual_stock_reports/4533_latest.md?ref=main

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
- entry_strategy_zh: 突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。
- position_sizing_zh: 半部位；部位大小需依支撐距離、波動與模型確認度控制。
- add_position_strategy_zh: 接近支撐時可建立第一筆部位、守住 23EMA 後再評估加碼、站回 23EMA 後再評估加碼、放量突破後再評估加碼、接近前高或壓力區可分批停利、量價失敗或爆量不漲時降低部位、跌破 23EMA 且 1 至 3 日內無法收回時退出、跌破近期低點時退出、營收或財報明顯轉弱時降低部位、TDCC 與價格同步轉弱時退出
- take_profit_strategy_zh: 接近前高或壓力區可分批停利；若爆量不漲、長上影或量價背離，需降低部位。
- risk_control_zh: 若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。
- post_entry_watch_zh: 下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱
- final_decision_zh: 符合 區間內轉強 / 挑戰前高觀察，價格結構尚未破壞，操作評級為「可分批買進」。 進場策略：突破後順勢追蹤；可依「半部位」建立第一筆，不需把買進後追蹤項目全部當成買進前條件。 追蹤項目：下一次月營收、下一次 TDCC 更新、23EMA 是否守住或快速站回、量價是否延續確認、前高突破品質、族群與 benchmark 強弱、事件催化是否延續、權證是否過熱 風控：若跌破 23EMA 或支撐區、量價失敗、營收轉弱或 TDCC 同步轉弱，需降低部位。

## ACTION_DECISION
- pdf_visible: false
- internal_use_only: true
- action_rating: scale_in
- action_rating_label_zh: 可分批買進
- confidence_level: medium
- thesis_state: breakout_initial
- entry_style: breakout_follow
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
- date: 20260702
- open: 28.7
- high: 31.2
- low: 28.25
- close: 31.2
- volume: 5432000
- ma5: 28.56
- ema23_primary: 29.86
- distance_to_ema23_pct: 4.48
- ma20: 29.74
- ma60: 30.9
- ma120: 31.13
- return_5d: 9.28
- return_20d: -2.19
- volume_ratio: 4.17
- distance_to_ma20_pct_auxiliary: 4.9
- distance_to_high_60_pct: -11.61

## Recent Price Preview
This is a short preview only. For K-line/chart work read price_window_180_txt_* above.
```csv
date,open,high,low,close,volume,ema23,distance_to_ema23_pct,ma20,ma60,volume_ratio
20260604,31.75,31.85,31.2,31.8,32000,32.01,-0.65,32.05,31.74,0.02
20260605,32.5,33.25,30.65,31,32000,31.92,-2.89,32.07,31.72,0.03
20260608,28.1,29.3,28,29.15,2055000,31.69,-8.02,31.94,31.66,1.6
20260609,30.8,31.15,30,31.05,1598000,31.64,-1.86,31.94,31.62,1.23
20260610,31,31.8,29.75,29.85,1866000,31.49,-5.21,31.87,31.56,1.43
20260611,29.85,30.2,28.85,30.15,1150000,31.38,-3.91,31.84,31.51,0.9
20260612,31.75,31.9,30.65,30.75,1489000,31.33,-1.84,31.77,31.46,1.41
20260615,31.2,31.35,30.65,30.75,965000,31.28,-1.69,31.71,31.42,1.13
20260616,31.1,31.1,30.05,30.2,792000,31.19,-3.17,31.63,31.39,1.01
20260617,30.3,30.4,29.85,29.9,831000,31.08,-3.8,31.54,31.37,1.13
20260618,30.1,30.4,29.85,30.2,1097000,31.01,-2.6,31.42,31.34,1.8
20260622,30.7,30.95,30.2,30.3,1655000,30.95,-2.09,31.26,31.28,2.4
20260623,30.75,30.75,29.25,29.35,1234000,30.81,-4.75,31.04,31.2,1.65
20260624,29.25,29.45,28.8,29.05,1102000,30.67,-5.28,30.78,31.13,1.37
20260625,29.15,29.3,28.5,28.55,1154000,30.49,-6.37,30.61,31.06,1.34
20260626,28.55,28.6,27.15,27.3,1643000,30.23,-9.68,30.38,31,1.75
20260629,27.35,28.15,27.35,27.65,542000,30.01,-7.87,30.15,30.95,0.56
20260630,28.25,28.5,27.95,28.25,647000,29.86,-5.4,29.93,30.9,0.65
20260701,28.55,28.65,27.95,28.4,740000,29.74,-4.51,29.78,30.87,0.72
20260702,28.7,31.2,28.25,31.2,5432000,29.86,4.48,29.74,30.9,4.17
```

## Latest TDCC Snapshot
- as_of_date: 20260626
- over_400_ratio: 29.11
- over_600_ratio: 26.23
- over_800_ratio: 23.59
- over_1000_ratio: 23.03
- over_400_change_1w: -0.07
- over_800_change_1w: -0.06
- over_1000_change_1w: -0.06
- tdcc_consecutive_up_weeks: 0
- all_thresholds_up: False
- high_thresholds_up: False

## TDCC Preview
This is a short preview only. For all available weekly TDCC rows read tdcc_window_txt_* above.
```csv
as_of_date,over_400_ratio,over_400_change_1w,over_800_ratio,over_800_change_1w,over_1000_ratio,over_1000_change_1w,tdcc_consecutive_up_weeks,all_thresholds_up,high_thresholds_up
20260430,27.33,,24.06,,22.95,,0,False,False
20260508,27.92,0.59,24.84,0.78,24.28,1.33,1,True,True
20260515,28.39,0.47,24.74,-0.1,24.18,-0.1,2,False,False
20260522,28.94,0.55,25.44,0.7,24.35,0.17,3,True,True
20260529,29.21,0.27,25.51,0.07,23.9,-0.45,4,False,True
20260605,29.32,0.11,24.32,-1.19,23.16,-0.74,5,False,False
20260612,29.39,0.07,23.63,-0.69,23.07,-0.09,6,False,False
20260618,29.18,-0.21,23.65,0.02,23.09,0.02,7,False,True
20260626,29.11,-0.07,23.59,-0.06,23.03,-0.06,0,False,False
```

## Candidate Context
| date | stock_id | stock_name | category | category_cn | score | rank | revaluation_priority | pattern_stage | tdcc_judgement | warrant_flow_signal | repeat_appear_label | catalyst_summary |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 4533 | 協易機 | range_rebound | 區間內轉強 / 挑戰前高觀察 | 69.0 |  |  | platform_breakout |  |  | first_seen | 1.董事會決議日期:115/07/01 2.私募有價證券種類:普通股 3.私募對象及其與公司間關係: (1) 本公司115/06/22董事會授權董事長洽定應募人，現洽定應募人為     「台企再造壹私募股權投資有限合夥」。 (2) 應募人為策略性投資人。 (3) 應募人與公司間關係：無。  4.私募股數或張數:20,000,000股 5.得私募額度:  於不超過20,000,000股額度內私募普通股，私募總金額依實際私募情形授權董事會辦理 6.私募價格訂定之依據及合理性:  (1)係依本公司115年6月11日股東常會通過定價原則，私募普通股每股價格不得低於參     考價格之八成。  (2)以董事會召開日115年6月22日為定價日，以定價日前1、3、或5個營業日擇一計算     之普通股收盤價簡單算數平均數扣除無償配股除權及配息，並加回減資反除權後之     股價分別為30.20元、30.10元及30.36元，與定價日前30個營業日普通股收盤價簡     單算數平均數扣除無償配股除權及配息，並加回減資反除權後之股價31.47元，二     者取較高31.47元為參考價之訂定基準。  (3)本次實際私募價格為26.75元，未低於股東常會決議實際私募價格不得低於參考價     格八成。  7.本次私募資金用途:  充實營運資金、改善財務結構或其他因應本公司未來發展之資金需求。 8.不採用公開募集之理由:  相較於公開募集，私募有價證券於3年內不得自由轉讓之規定將更可確保公司與策略性  投資夥伴間之長期合作關係；另透過授權董事會視公司營運實際需求辦理私募，亦將  有效提高公司籌資之機動性與靈活性。 9.獨立董事反對或保留意見:無 10.實際定價日:115/06/22 11.參考價格:31.47元 12.實際私募價格、轉換或認購價格:26.75元 13.本次私募新股之權利義務:   本私募普通股案中所發行之新股其權利義務與原股份相同；惟依證券交易法第43條之8   規定，本私募普通股於交付後3年內，除符合法令規定之特定情形外不得自由轉讓；本   公司亦擬於該私募普通股交付滿3年後，授權董事會於適當時機依相關法令規定向主管   機關申請補辦公開發行及上市(櫃)交易。 14.附有轉換、交換或認股者，其換股基準日:不適用 15.附有轉換、交換或認股者，對股權可能稀釋情形:不適用 16.附有轉換或認股者，於私募公司債交付且假設全數轉換或認購普通股後對上櫃普通股 股權比率之可能影響（上櫃普通股數A、A/已發行普通股）:不適用 17.前項預計上櫃普通股未達500萬股且未達25%者，請說明股權流通性偏低之因應措施: 不適用 18.其他應敘明事項:依115/6/22董事會授權董事長於115/7/1洽定應募人。；calendar event: monthly_revenue_expected_window on 20260701; status=expected_window; proximity=recent |

## Repeat Appearance Context
| signal_date | stock_id | stock_name | consecutive_appear_days_any_category | consecutive_appear_days_same_category | appear_count_5d | appear_count_10d | appear_count_20d | repeat_appear_label | repeat_appear_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20260702 | 4533 | 協易機 | 1 | 1 | 1 | 1 | 1 | first_seen | 首次上榜，屬新訊號，需確認量價、TDCC 與 benchmark 表現。 |

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
