# Model Operation Readiness

- generated_at: `2026-06-15 15:22:23 Asia/Taipei`
- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries
- rule: `approved_for_daily=False` means no formal daily buy/sell directive is approved
- rule: `presentation_allowed=True` only permits research-derived historical reference rendering
- rule: PDF/packet integration must render adapter artifacts and must not recalculate operation rules

## operation_module_status

| operation_module_status | count |
| --- | --- |
| baseline_only_no_validated_operation_module | 9 |
| research_reference_ready | 1 |

## daily_adapter_status

| daily_adapter_status | count |
| --- | --- |
| not_started | 9 |
| ready_research_reference_only | 1 |

## approved_for_daily

| approved_for_daily | count |
| --- | --- |
| False | 10 |

## presentation_allowed

| presentation_allowed | count |
| --- | --- |
| False | 9 |
| True | 1 |

## Status Table

| model_id | parity_status | operation_module_status | daily_adapter_status | approved_for_daily | presentation_allowed | operation_directive_level | pdf_integration_status | packet_integration_status | blocker | status_note_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout | production_parity | research_reference_ready | ready_research_reference_only | False | True | research_reference_only | pending_pdf_renderer | pending_packet_renderer | PDF/packet renderer pending; operation section is a research reference, not a formal buy/sell directive | 放量攻擊已有研究統計操作參考與 daily adapter；只能呈現為歷史證據參考，不是正式買賣指令。PDF/packet 之後只能讀 adapter artifact，不可重算規則。 |
| hot_theme_pullback | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| near_high_neckline_challenge | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | neckline-specific fields and already-confirmed-breakout flags are not fully backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| platform_strengthening | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | platform_base_flag and platform width fields are not fully point-in-time backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| price_pullback_23ema | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | support/platform entry flags are not fully backfilled in the historical research frame | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| pullback_short_reclaim | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| revenue_unreacted_range | proxy_only | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_short_term_continuation_d5_d10 | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| tdcc_stealth_accumulation | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | tdcc_price_phase is not fully available historically for every signal date | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
| w_bottom_right_side | production_proxy | baseline_only_no_validated_operation_module | not_started | False | False | no_operation_directive | not_started | not_started | full production W-bottom detector is row/context based and not yet reused by the research grid | 目前只完成 research baseline/parameter 對照；尚未有 validated operation module，不可產生買進、賣出、停損或排名操作建議。 |
