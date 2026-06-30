# Model Operation Readiness

- generated_at: `2026-07-01 04:05:31 Asia/Taipei`
- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries
- rule: `approved_for_daily=True` requires an explicit approved operation artifact
- rule: raw research evidence rows can remain research-only even after an operation module is approved
- rule: PDF/packet integration 必須 render adapter artifact，不得重新計算操作規則

## operation_module_status

| operation_module_status | count |
| --- | --- |
| baseline_only_no_validated_operation_module | 5 |
| approved_operation_v1 | 2 |
| approved_operation_v2 | 1 |
| operation_candidate_v1_discussion_ready_pending_latest_research_frame | 1 |

## daily_adapter_status

| daily_adapter_status | count |
| --- | --- |
| not_started | 5 |
| ready_approved_operation_guidance | 2 |
| ready_empty_no_operation_rows | 1 |
| blocked_latest_research_frame | 1 |

## approved_for_daily

| approved_for_daily | count |
| --- | --- |
| False | 6 |
| True | 3 |

## presentation_allowed

| presentation_allowed | count |
| --- | --- |
| False | 6 |
| True | 3 |

## Status Table

| model_id | parity_status | operation_module_status | daily_adapter_status | approved_for_daily | approval_status | operation_module_id | approval_version | presentation_allowed | operation_directive_level | pdf_integration_status | packet_integration_status | blocker | status_note_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout | production_parity | approved_operation_v1 | ready_approved_operation_guidance | True | approved_for_daily_v1 | volume_breakout_confirmed_operation_v1 | volume_breakout_operation_v1_20260615 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | PDF/packet 已接每日 adapter 資料成品 | 放量攻擊 v1 已由 approved_operation_patterns 批准為 daily 操作建議；只有已確認列可列買進排名，待確認列只作觀察。PDF/packet 仍只能讀每日 adapter 資料成品。 |
| w_bottom_right_side | production_parity | approved_operation_v2 | ready_approved_operation_guidance | True | approved_for_daily_v2 | w_bottom_early_entry_operation_v2 | w_bottom_early_entry_operation_v2_20260629 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | W-bottom early-entry operation v2 adapter is ready; positive-return rate and average return must be labeled as D+20/D+40 operation metrics | W底右低點早期進場 v2 已由 approved_operation_patterns 批准；此模型使用標題下方證據，不共用放量攻擊 operation section adapter。 |
| neckline_volume_breakout_confirmation | production_parity | approved_operation_v1 | ready_empty_no_operation_rows | True | approved_for_daily_v1 | neckline_strict_45_signal_90_score_v1 | neckline_strict_45_signal_90_score_v1_20260629 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | neckline strict 45 signal / 90 score operation adapter is ready; operation-rule win rate and neutral-inclusive success rate must be labeled separately | W底頸線帶量突破 v1 已由 approved_operation_patterns 批准；45日 context 是入選訊號，90日 context 只作分數與風險調整；此模型使用標題下方證據，不共用放量攻擊 operation section adapter，也不混入其他頸線型態。 |
| price_pullback_23ema | production_proxy | operation_candidate_v1_discussion_ready_pending_latest_research_frame | blocked_latest_research_frame | False | pending_research_freshness_and_promotion_pr | price_pullback_23ema_prev20_breakout_stop_v1 | price_pullback_23ema_operation_candidate_v1_20260630 | False | no_operation_directive | blocked_latest_research_frame | blocked_latest_research_frame | latest research frame freshness pending: snapshots=10, latest_snapshot=20260630, production_candidate_universe_replay_exact=True, missing_research_dates=1 | price_pullback_23ema 已選出 operation candidate v1：先有 production proxy 訊號，且同日符合大戶高門檻增加與 20 日漲幅 0% 到 25%；買點為次日開盤，勝利為 D+20 前盤中突破訊號日前 20 日高點，失敗為連續 4 日收盤低於 MA20/EMA23 較低者 4%。daily row replay 已足夠開始模型決策討論；仍需補 latest research frame freshness 與 promotion/sync PR。daily production row replay 已用 dated all_candidates/source-row 通過 10 個 published snapshots，published/proxy row gap=0；仍有 1 個 latest snapshot 缺 research frame 日期，所以不能 promotion 或產生 production 操作建議，但可以開始模型決策討論。所以不得產生 production 買進、賣出、停損或排名操作建議。 |
| hot_theme_pullback | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| pullback_short_reclaim | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| revenue_unreacted_range | proxy_only | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_short_term_continuation_d5_d10 | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_stealth_accumulation | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | tdcc_price_phase is not fully available historically for every signal date | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
