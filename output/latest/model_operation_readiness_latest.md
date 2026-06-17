# Model Operation Readiness

- generated_at: `2026-06-18 04:13:07 Asia/Taipei`
- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries
- rule: `approved_for_daily=True` requires an explicit approved operation artifact
- rule: raw research evidence rows can remain research-only even after an operation module is approved
- rule: PDF/packet integration 必須 render adapter artifact，不得重新計算操作規則

## operation_module_status

| operation_module_status | count |
| --- | --- |
| baseline_only_no_validated_operation_module | 9 |
| approved_operation_v1 | 1 |

## daily_adapter_status

| daily_adapter_status | count |
| --- | --- |
| not_started | 9 |
| ready_approved_operation_guidance | 1 |

## approved_for_daily

| approved_for_daily | count |
| --- | --- |
| False | 9 |
| True | 1 |

## presentation_allowed

| presentation_allowed | count |
| --- | --- |
| False | 9 |
| True | 1 |

## Status Table

| model_id | parity_status | operation_module_status | daily_adapter_status | approved_for_daily | approval_status | operation_module_id | approval_version | presentation_allowed | operation_directive_level | pdf_integration_status | packet_integration_status | blocker | status_note_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout | production_parity | approved_operation_v1 | ready_approved_operation_guidance | True | approved_for_daily_v1 | volume_breakout_confirmed_operation_v1 | volume_breakout_operation_v1_20260615 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | PDF/packet 已接每日 adapter 資料成品 | 放量攻擊 v1 已由 approved_operation_patterns 批准為 daily 操作建議；只有已確認列可列買進排名，待確認列只作觀察。PDF/packet 仍只能讀每日 adapter 資料成品。 |
| hot_theme_pullback | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| near_high_neckline_challenge | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | neckline-specific fields and already-confirmed-breakout flags are not fully backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| platform_strengthening | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | platform_base_flag and platform width fields are not fully point-in-time backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| price_pullback_23ema | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | support/platform entry flags are not fully backfilled in the historical research frame | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| pullback_short_reclaim | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| revenue_unreacted_range | proxy_only | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_short_term_continuation_d5_d10 | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_stealth_accumulation | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | tdcc_price_phase is not fully available historically for every signal date | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| w_bottom_right_side | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | full production W-bottom detector is row/context based and not yet reused by the research grid | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
