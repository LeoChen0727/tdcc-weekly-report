# Model Operation Readiness

- generated_at: `2026-07-11 23:59:34 Asia/Taipei`
- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries
- rule: `approved_for_daily=True` requires an explicit approved operation artifact
- rule: raw research evidence rows can remain research-only even after an operation module is approved
- rule: PDF/packet integration 必須 render adapter artifact，不得重新計算操作規則

## operation_module_status

| operation_module_status | count |
| --- | --- |
| approved_operation_v1 | 5 |
| baseline_only_no_validated_operation_module | 5 |
| approved_operation_v2 | 1 |

## daily_adapter_status

| daily_adapter_status | count |
| --- | --- |
| not_started | 5 |
| ready_approved_operation_guidance | 4 |
| ready_empty_no_operation_rows | 2 |

## approved_for_daily

| approved_for_daily | count |
| --- | --- |
| True | 6 |
| False | 5 |

## presentation_allowed

| presentation_allowed | count |
| --- | --- |
| True | 6 |
| False | 5 |

## Status Table

| model_id | parity_status | operation_module_status | daily_adapter_status | approved_for_daily | approval_status | operation_module_id | approval_version | presentation_allowed | operation_directive_level | pdf_integration_status | packet_integration_status | blocker | status_note_zh |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| volume_range_breakout_v2_low_position_volume_attack | production_parity | approved_operation_v1 | ready_approved_operation_guidance | True | approved_for_daily_v1 | volume_range_breakout_v2_low_position_operation_v1 | volume_range_breakout_v2_formal_operation_20260709 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | v2 volume breakout operation adapter is ready | v2 放量攻擊正式模型：模型條件加 close-only 確認就是買入 gate；TDCC、MA60/MA120、EMA23 距離僅能作分層或加分，不得作 hidden gate。 |
| volume_range_breakout_v2_mid_position_momentum_attack | production_parity | approved_operation_v1 | ready_empty_no_operation_rows | True | approved_for_daily_v1 | volume_range_breakout_v2_mid_position_operation_v1 | volume_range_breakout_v2_formal_operation_20260709 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | v2 volume breakout operation adapter is ready | v2 放量攻擊正式模型：模型條件加 close-only 確認就是買入 gate；TDCC、MA60/MA120、EMA23 距離僅能作分層或加分，不得作 hidden gate。 |
| volume_range_breakout_v2_high_position_volume_attack | production_parity | approved_operation_v1 | ready_approved_operation_guidance | True | approved_for_daily_v1 | volume_range_breakout_v2_high_position_operation_v1 | volume_range_breakout_v2_high_position_operation_20260710 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | v2 volume breakout operation adapter is ready | v2 放量攻擊正式模型：模型條件加 close-only 確認就是買入 gate；TDCC、MA60/MA120、EMA23 距離僅能作分層或加分，不得作 hidden gate。 |
| w_bottom_right_side | production_parity | approved_operation_v2 | ready_approved_operation_guidance | True | approved_for_daily_v2 | w_bottom_early_entry_operation_v2 | w_bottom_early_entry_operation_v2_20260629 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | W-bottom operation adapter is ready | W底右側模型已核准為 daily operation guidance，PDF 僅能消費 model-owned operation adapter。 |
| neckline_volume_breakout_confirmation | production_parity | approved_operation_v1 | ready_empty_no_operation_rows | True | approved_for_daily_v1 | neckline_strict_45_signal_90_score_v1 | neckline_strict_45_signal_90_score_v1_20260629 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | neckline operation adapter is ready | W底頸線帶量突破確認模型已核准為 daily operation guidance，PDF 僅能消費 model-owned operation adapter。 |
| price_pullback_23ema | production_parity | approved_operation_v1 | ready_approved_operation_guidance | True | approved_for_daily_v1 | price_pullback_23ema_prev20_breakout_stop_v1 | price_pullback_23ema_operation_v1_20260703 | True | approved_daily_operation_guidance | pdf_integrated_daily_adapter | packet_integrated_daily_adapter | price_pullback_23ema operation adapter is ready | 23EMA回檔模型已核准為 daily operation guidance，PDF 僅能消費 model-owned operation adapter。 |
| hot_theme_pullback | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily hot-theme labels are not fully backfilled as point-in-time model-layer fields | 目前只有 research baseline/parameter 對照，沒有 validated operation module，不得產生買入、出場、停損或排序操作建議。 |
| pullback_short_reclaim | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled | 目前只有 research baseline/parameter 對照，沒有 validated operation module，不得產生買入、出場、停損或排序操作建議。 |
| revenue_unreacted_range | proxy_only | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | strong_revenue gate requires model-specific research matrix, contract update, exact parity, and promotion PR before formal use | 目前只有 research baseline/parameter 對照，沒有 validated operation module，不得產生買入、出場、停損或排序操作建議。 |
| tdcc_short_term_continuation_d5_d10 | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies | 目前只有 research baseline/parameter 對照，沒有 validated operation module，不得產生買入、出場、停損或排序操作建議。 |
| tdcc_stealth_accumulation | production_proxy | baseline_only_no_validated_operation_module | not_started | False | not_started |  |  | False | no_operation_directive | not_started | not_started | tdcc_price_phase is not fully available historically for every signal date | 目前只有 research baseline/parameter 對照，沒有 validated operation module，不得產生買入、出場、停損或排序操作建議。 |
