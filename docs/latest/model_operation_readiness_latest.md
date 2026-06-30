# Model Operation Readiness

- generated_at: `2026-06-30 10:05:07 Asia/Taipei`
- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries
- rule: `approved_for_daily=True` requires an explicit approved operation artifact
- rule: raw research evidence rows can remain research-only even after an operation module is approved
- rule: PDF/packet integration 必須 render adapter artifact，不得重新計算操作規則

## operation_module_status

| operation_module_status | count |
| --- | --- |
| baseline_only_no_validated_operation_module | 6 |
| approved_operation_v1 | 2 |
| approved_operation_v2 | 1 |

## daily_adapter_status

| daily_adapter_status | count |
| --- | --- |
| not_started | 6 |
| model_header_evidence_ready | 2 |
| ready_approved_operation_guidance | 1 |

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
| w_bottom_right_side | production_parity | approved_operation_v2 | model_header_evidence_ready | True | approved_for_daily_v2 | w_bottom_early_entry_operation_v2 | w_bottom_early_entry_operation_v2_20260629 | True | approved_daily_operation_guidance | pdf_model_header_evidence_ready | packet_model_header_evidence_ready | W-bottom early-entry operation v2 approval is ready; positive-return rate and average return must be labeled as D+20/D+40 operation metrics | W底右低點早期進場 v2 已由 approved_operation_patterns 批准；此模型使用標題下方證據，不共用放量攻擊 operation section adapter。 |
| neckline_volume_breakout_confirmation | production_parity | approved_operation_v1 | model_header_evidence_ready | True | approved_for_daily_v1 | neckline_strict_45_signal_90_score_v1 | neckline_strict_45_signal_90_score_v1_20260629 | True | approved_daily_operation_guidance | pdf_model_header_evidence_ready | packet_model_header_evidence_ready | neckline strict 45 signal / 90 score operation approval is ready; operation-rule win rate and neutral-inclusive success rate must be labeled separately | W底頸線帶量突破 v1 已由 approved_operation_patterns 批准；45日 context 是入選訊號，90日 context 只作分數與風險調整；此模型使用標題下方證據，不共用放量攻擊 operation section adapter，也不混入其他頸線型態。 |
| hot_theme_pullback | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| price_pullback_23ema | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | as-published daily candidate row parity and a validated operation module are still pending | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| pullback_short_reclaim | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| revenue_unreacted_range | proxy_only | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_short_term_continuation_d5_d10 | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_stealth_accumulation | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | tdcc_price_phase is not fully available historically for every signal date | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
