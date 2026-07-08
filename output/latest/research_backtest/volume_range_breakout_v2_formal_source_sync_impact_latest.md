# Volume Range Breakout V2 Formal Source Sync Impact

- research_id: `volume_range_breakout_v2_formal_source_sync_impact`
- artifact_version: `volume_range_breakout_v2_formal_source_sync_impact_20260708`
- advisory_status: `warning_research_variant_only`
- production_readiness: `not_production_ready_research_only`
- approved_for_daily: `False`
- This is a non-writing research-only formal source sync impact audit.
- It does not rewrite `volume_breakout_formal_operation_events.csv` and does not change `stock_model_contract_registry.csv`.
- Discussion point: current formal producer would add rows absent from the existing formal artifact, including rows inside the existing artifact window.

## Summary

| audit_key | sample_size | current_formal_rows | existing_formal_rows | current_minus_existing_unique_keys | existing_minus_current_unique_keys | inside_existing_window_rows | after_existing_window_rows | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| current_vs_existing_formal_events | 47 | 3292 | 3245 | 39 | 0 | 7 | 40 | source_sync_required_before_promotion |
| inside_existing_artifact_window_rows | 7 | 3292 | 3245 | 39 | 0 | 7 | 40 | requires_user_discussion_source_sync_scope |
| after_existing_artifact_window_rows | 40 | 3292 | 3245 | 39 | 0 | 7 | 40 | expected_freshness_extension_requires_refresh |

## Inside Existing Artifact Window

| stock_id | stock_name | signal_date | confirmation_date | selected_trigger_id | entry_date | exit_date | return_pct | price_history_rows | sync_impact_classification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8077 | 洛碁 | 20260528 | 20260529 | pullback_5ma_confirmed | 20260601 | 20260615 | 4.9689 | 90 | inside_existing_artifact_window_source_sync_required |
| 8077 | 洛碁 | 20260529 | 20260601 | pullback_5ma_confirmed | 20260602 | 20260616 | 1.3265 | 90 | inside_existing_artifact_window_source_sync_required |
| 8077 | 洛碁 | 20260603 | 20260604 | pullback_5ma_confirmed | 20260605 | 20260612 | -10.2564 | 90 | inside_existing_artifact_window_source_sync_required |
| 8077 | 洛碁 | 20260604 | 20260611 | pullback_10ma_confirmed | 20260612 | 20260612 | -3.1008 | 90 | inside_existing_artifact_window_source_sync_required |
| 9914 | 美利達 | 20260611 | 20260622 | pullback_5ma_confirmed | 20260623 | 20260706 | 2.5676 | 299 | inside_existing_artifact_window_source_sync_required |
| 3290 | 東浦 | 20260616 | 20260623 | pullback_5ma_confirmed | 20260624 | 20260707 | -1.9174 | 164 | inside_existing_artifact_window_source_sync_required |
| 9928 | 中視 | 20260617 | 20260623 | pullback_5ma_confirmed | 20260624 | 20260707 | -2.381 | 299 | inside_existing_artifact_window_source_sync_required |

## Freshness Extension

| stock_id | stock_name | signal_date | confirmation_date | selected_trigger_id | entry_date | exit_date | return_pct | price_history_rows | sync_impact_classification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1905 | 華紙 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260706 | -5.3371 | 299 | after_existing_artifact_window_freshness_extension |
| 2061 | 風青 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260706 | 33.7229 | 164 | after_existing_artifact_window_freshness_extension |
| 2302 | 麗正 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260623 | -4.3203 | 299 | after_existing_artifact_window_freshness_extension |
| 2342 | 茂矽 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260626 | -12.3077 | 299 | after_existing_artifact_window_freshness_extension |
| 2342 | 茂矽 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260626 | -12.3077 | 299 | after_existing_artifact_window_freshness_extension |
| 2492 | 華新科 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260629 | -22.3256 | 299 | after_existing_artifact_window_freshness_extension |
| 2492 | 華新科 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260629 | -22.3256 | 299 | after_existing_artifact_window_freshness_extension |
| 2890 | 永豐金 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260706 | 2.5 | 299 | after_existing_artifact_window_freshness_extension |
| 3090 | 日電貿 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260623 | -1.5576 | 298 | after_existing_artifact_window_freshness_extension |
| 3290 | 東浦 | 20260618 | 20260623 | pullback_5ma_confirmed | 20260624 | 20260624 | -2.3599 | 164 | after_existing_artifact_window_freshness_extension |
| 3624 | 光頡 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260623 | -6.686 | 164 | after_existing_artifact_window_freshness_extension |
| 3624 | 光頡 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260623 | -6.686 | 164 | after_existing_artifact_window_freshness_extension |
| 3624 | 光頡 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260623 | -6.686 | 164 | after_existing_artifact_window_freshness_extension |
| 4551 | 智伸科 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260629 | -4.4248 | 299 | after_existing_artifact_window_freshness_extension |
| 5328 | 華容 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260624 | -9.2982 | 164 | after_existing_artifact_window_freshness_extension |
| 5489 | 彩富 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260706 | 18.4725 | 164 | after_existing_artifact_window_freshness_extension |
| 6259 | 百徽 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260706 | -1.5248 | 163 | after_existing_artifact_window_freshness_extension |
| 6742 | 澤米 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260626 | -4.3478 | 299 | after_existing_artifact_window_freshness_extension |
| 6742 | 澤米 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260626 | -4.3478 | 299 | after_existing_artifact_window_freshness_extension |
| 6834 | 天二科技 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260706 | 14.2857 | 299 | after_existing_artifact_window_freshness_extension |
| 8081 | 致新 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260702 | -16.0819 | 299 | after_existing_artifact_window_freshness_extension |
| 8121 | 越峰 | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260624 | -13.8889 | 164 | after_existing_artifact_window_freshness_extension |
| 8476 | 台境* | 20260618 | 20260622 | next_day_break_signal_high_confirmed | 20260623 | 20260706 | 5.0439 | 299 | after_existing_artifact_window_freshness_extension |
| 1303 | 南亞 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260624 | 0.0 | 299 | after_existing_artifact_window_freshness_extension |
| 2303 | 聯電 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260629 | -6.9767 | 299 | after_existing_artifact_window_freshness_extension |
| 2340 | 台亞 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260624 | -1.6393 | 299 | after_existing_artifact_window_freshness_extension |
| 2340 | 台亞 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260624 | -1.6393 | 299 | after_existing_artifact_window_freshness_extension |
| 2481 | 強茂 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260626 | -5.63 | 299 | after_existing_artifact_window_freshness_extension |
| 3041 | 揚智 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260626 | -5.9016 | 299 | after_existing_artifact_window_freshness_extension |
| 3041 | 揚智 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260626 | -5.9016 | 299 | after_existing_artifact_window_freshness_extension |
| 3465 | 進泰電子 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260624 | 0.0 | 164 | after_existing_artifact_window_freshness_extension |
| 4551 | 智伸科 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260629 | -7.6923 | 299 | after_existing_artifact_window_freshness_extension |
| 5489 | 彩富 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260707 | 3.8772 | 164 | after_existing_artifact_window_freshness_extension |
| 6435 | 大中 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260624 | -2.6499 | 164 | after_existing_artifact_window_freshness_extension |
| 6620 | 漢達 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260624 | -0.9912 | 128 | after_existing_artifact_window_freshness_extension |
| 6715 | 嘉基 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260624 | -6.5217 | 299 | after_existing_artifact_window_freshness_extension |
| 6834 | 天二科技 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260707 | 7.2398 | 299 | after_existing_artifact_window_freshness_extension |
| 8261 | 富鼎 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260629 | -5.2104 | 299 | after_existing_artifact_window_freshness_extension |
| 8261 | 富鼎 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260629 | -5.2104 | 299 | after_existing_artifact_window_freshness_extension |
| 9949 | 琉園 | 20260622 | 20260623 | next_day_break_signal_high_confirmed | 20260624 | 20260707 | 7.9848 | 163 | after_existing_artifact_window_freshness_extension |

## Outputs

- summary_csv: `output/latest/research_backtest/volume_range_breakout_v2_formal_source_sync_impact_latest.csv`
- detail_csv: `output/latest/research_backtest/volume_range_breakout_v2_formal_source_sync_impact_detail_latest.csv`
- detail_rows: `47`
