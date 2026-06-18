# Daily Volume Breakout Operation Section Contract

This contract is the handoff from production/model code to the PDF/packet renderer.

The PDF renderer must read:

- `output/latest/daily_volume_breakout_operation_section_latest.csv`
- `output/latest/daily_volume_breakout_operation_section_latest.md`

The adapter also emits an audit-only artifact:

- `output/latest/daily_volume_breakout_operation_evidence_audit_latest.csv`
- `output/latest/daily_volume_breakout_operation_evidence_audit_latest.md`

This audit explains why confirmed/active candidates were included or excluded. It is not a PDF source.

The PDF renderer must not read these research artifacts directly:

- `output/latest/volume_breakout_operation_pdf_preview_latest.csv`
- `output/latest/volume_breakout_confirmed_operation_rank_latest.csv`
- `output/latest/volume_breakout_pending_operation_queue_latest.csv`
- `output/latest/volume_breakout_formal_operation_lifecycle_latest.csv`
- `output/latest/historical_pattern_operation_registry_latest.csv`
- `output/latest/approved_operation_patterns_latest.csv`
- `output/latest/daily_volume_breakout_operation_evidence_audit_latest.csv`
- `output/latest/volume_breakout_buy_signal_grid_latest.csv`
- `output/latest/volume_breakout_buy_signal_best_candidates_latest.csv`
- `output/latest/volume_breakout_buy_signal_evidence_registry_latest.csv`

The adapter may read only these operation sources:

- `output/latest/daily_candidate_model_signals_for_report_latest.csv`
- `output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv`
- `data/stock_price_history/{stock_id}.csv`
- `output/latest/volume_breakout_formal_operation_backtest_latest.csv`
- `output/latest/approved_operation_patterns_latest.csv`

Research/backtest may also emit `output/latest/volume_breakout_formal_operation_lifecycle_latest.csv`
to audit `pending_confirmation`, `confirmed_operation`, `active_operation`, and `expired`
states. That lifecycle artifact is not a PDF or daily adapter source.

## Scope

- `model_id` is always `volume_range_breakout`.
- The artifact is a production operation adapter, not a PDF calculation layer and not a research/backtest runner.
- It must not run backtests inside `daily_full_pipeline.yml`.
- `output/latest/volume_breakout_formal_operation_backtest_latest.csv` is the only formal operation evidence source for daily confirmed/active guidance.
- Its win rate, average return, and median return must be computed only from `metric_sample_scope=mature_selected_operation_only` rows.
- Missing or empty formal operation evidence must fail validation; the PDF must not fabricate buy/stop/exit rows.
- Other stock models must not reuse this operation section, ranking, entry rule, stop rule, or exit rule.
- `approved_for_daily=True` means this adapter is allowed to present `volume_range_breakout` v1 operation guidance. It does not approve any other model.
- `approved_for_daily=True` is module-level approval, not row-level buy permission.
- The PDF renderer must use `buy_rank_eligible=True` plus `row_action_status=confirmed_buy_candidate` for buy-ranking rows.
- `pending_confirmation` rows must remain `buy_rank_eligible=False` even when `approved_for_daily=True`.
- The adapter must copy approval metadata from `approved_operation_patterns_latest.csv`; the PDF renderer must not read that approval table directly.
- `confirmed_operation` data rows must be positive evidence only. Weak-evidence confirmations must not be presented as daily buy guidance.
- `confirmed_operation` and `active_operation` data rows must use row-level evidence attribution. The adapter must match the selected trigger plus that stock's TDCC list type, rank bucket, and best available confluence row before copying sample size, win rate, average return, or median return.
- If no positive row-level evidence exists for a confirmed/active candidate, the adapter must exclude that candidate from the daily section and write an audit row with `included_in_daily_adapter=False`.
- The adapter must carry `operation_asof_date` and `operation_source_date_status` on every row.
- Data rows are valid only when `operation_asof_date` equals `daily_signal_date`, which is the daily report date from `main_price_date`.
- Operation data rows must have a stock-level taxonomy/basic industry source before they can be routed to a PDF line. Valid report memberships are only `mainstream`, `non_mainstream`, or both. The PDF renderer must not invent a report line when taxonomy/source data is missing.

## Required Approval Fields

The CSV must include these approval fields on every row:

- `approval_source`
- `approved_for_daily`
- `operation_module_approved_for_daily`
- `approval_status`
- `operation_module_id`
- `approval_version`
- `operation_directive_level`
- `row_action_status`
- `buy_rank_eligible`
- `buy_filter_id`
- `approval_note_zh`
- `operation_asof_date`
- `operation_source_date_status`
- `matched_trigger_ids`
- `selected_trigger_id`
- `selected_confirmation_date`
- `selected_trigger_priority`
- `operation_score`
- `tdcc_score`
- `pattern_score`
- `risk_penalty`
- `final_rank_score`
- `rank_reason_zh`
- `entry_rule_id`
- `entry_price_basis`
- `entry_date`
- `entry_price`
- `stop_loss_rule_id`
- `stop_loss_price`
- `stop_loss_label_zh`
- `exit_rule_id`
- `planned_holding_days`
- `operation_age_days`

For the approved v1 daily adapter, these fields must show:

- `approved_for_daily=True`
- `operation_module_approved_for_daily=True`
- `approval_status=approved_for_daily_v1`
- `operation_directive_level=approved_daily_operation_guidance`

Row-level meaning:

- `confirmed_operation` + `row_type=data` + `row_action_status=confirmed_buy_candidate` + `buy_rank_eligible=True`: eligible for the daily buy ranking table.
- `pending_confirmation` + `row_type=data` + `row_action_status=pending_confirmation` + `buy_rank_eligible=False`: display only as pending confirmation; no entry price and no buy ranking.
- `active_operation` + `row_type=data` + `row_action_status=active_operation` + `buy_rank_eligible=False`: already entered tracking from an earlier confirmed row; it is not a new buy ranking row.
- `empty_state` rows must use `row_action_status=empty_state` and `buy_rank_eligible=False`.

Operation field meaning:

- `final_rank_score` is the daily production ranking score for `volume_range_breakout`; PDF must render it and must not recalculate it.
- `operation_score`, `tdcc_score`, `pattern_score`, and `risk_penalty` are score components copied from the daily model layer for auditability.
- `entry_rule_id=confirmation_next_open` means a confirmed row uses the next trading day's open after the selected confirmation date.
- `entry_date` and `entry_price` are structured entry fields. They stay blank on `confirmed_operation` until the next trading day's open exists, are required on `active_operation` data rows, and must remain blank on `pending_confirmation`.
- `stop_loss_rule_id=signal_low_stop` means the stop basis is the signal-date low, displayed as `{M/D}最低點`.
- `exit_rule_id=signal_low_stop_or_fixed_10d_close` means exit at the stop first, otherwise fixed 10 trading-day close.
- `pending_confirmation` rows must not show an entry price; they may carry rule IDs only to describe the eventual rule after confirmation.

## Sections

The CSV always includes these `pdf_section` values for both `pdf_view=highlight` and `pdf_view=full`:

- `confirmed_operation`: confirmed operation rows.
- `pending_confirmation`: pending signal rows.
- `active_operation`: operation-in-progress rows.

Every view must include all three sections. A section may use `row_type=empty_state` only when that section has no data rows.

PDF display limits:

- `pdf_view=highlight` must render at most 10 `confirmed_operation` data rows, at most 5 `pending_confirmation` data rows, and at most 5 `active_operation` data rows after mainstream / non-mainstream report-line filtering.
- `pdf_view=full` must not apply these highlight limits; it should render all valid operation rows for the selected report line.
- These limits are presentation limits only. They must not change row lifecycle state, `buy_rank_eligible`, trigger evidence, model scores, model ranks, or the underlying adapter rows.

Lifecycle meaning:

- First daily model hit enters `pending_confirmation`.
- If a later trading day meets one confirmation trigger before invalidation, it enters `confirmed_operation` only on that confirmation report date.
- After the entry day starts, it enters `active_operation` until stop or the 10th trading-day holding limit.
- If a signal breaks its stop basis before confirmation, exceeds the confirmation window, lacks positive formal evidence, hits stop after entry, or exceeds the holding window, it must drop from the operation section.

## PDF Rule

The PDF side should only render rows from this artifact. It must not recalculate:

- entry timing
- stop basis
- exit rule
- ranking
- sample size
- win rate
- median return

If a row has `row_type=empty_state`, the PDF should still render the section heading and an empty table/message.
