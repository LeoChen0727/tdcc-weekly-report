# Daily Volume Breakout Operation Section Contract

This contract is the handoff from production/model code to the future PDF renderer.

The PDF renderer must read:

- `output/latest/daily_volume_breakout_operation_section_latest.csv`
- `output/latest/daily_volume_breakout_operation_section_latest.md`

The PDF renderer must not read these research artifacts directly:

- `output/latest/volume_breakout_operation_pdf_preview_latest.csv`
- `output/latest/volume_breakout_confirmed_operation_rank_latest.csv`
- `output/latest/volume_breakout_pending_operation_queue_latest.csv`
- `output/latest/historical_pattern_operation_registry_latest.csv`
- `output/latest/approved_operation_patterns_latest.csv`

## Scope

- `model_id` is always `volume_range_breakout`.
- The artifact is a production presentation adapter, not a research/backtest runner.
- It may consume latest available research outputs, but it must not run backtests inside `daily_full_pipeline.yml`.
- Missing or empty research inputs must produce explicit empty-state rows instead of blocking the daily pipeline.
- Other stock models must not reuse this operation section, ranking, entry rule, stop rule, or exit rule.
- `approved_for_daily=True` means this adapter is allowed to present `volume_range_breakout` v1 operation guidance. It does not approve any other model.
- `approved_for_daily=True` is module-level approval, not row-level buy permission.
- The PDF renderer must use `buy_rank_eligible=True` plus `row_action_status=confirmed_buy_candidate` for buy-ranking rows.
- `pending_confirmation` rows must remain `buy_rank_eligible=False` even when `approved_for_daily=True`.
- The adapter must copy approval metadata from `approved_operation_patterns_latest.csv`; the PDF renderer must not read that approval table directly.
- `confirmed_operation` data rows must be positive evidence only. Weak-evidence confirmed rows from research previews must not be presented as daily buy guidance.
- The adapter must carry `operation_asof_date` and `operation_source_date_status` on every row.
- Confirmed-operation rows from research previews are valid only when `operation_asof_date` equals `daily_signal_date`, which is the daily report date. Stale operation research previews must not enter the daily PDF or packet as confirmed buy guidance.
- First-time or unconfirmed `volume_range_breakout` production model hits enter `pending_confirmation`.
- `pending_confirmation` rows come from the current daily model-signal artifact, keep `buy_rank_eligible=False`, and must not be rendered as buy-rank rows.
- Only rows that later satisfy the operation confirmation condition enter `confirmed_operation`.
- `confirmed_operation` buy-rank rows must carry `row_action_status=confirmed_buy_candidate` and `buy_rank_eligible=True`.
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

For the approved v1 daily adapter, these fields must show:

- `approved_for_daily=True`
- `operation_module_approved_for_daily=True`
- `approval_status=approved_for_daily_v1`
- `operation_directive_level=approved_daily_operation_guidance`

Row-level meaning:

- `confirmed_operation` + `row_type=data` + `row_action_status=confirmed_buy_candidate` + `buy_rank_eligible=True`: eligible for the daily buy ranking table.
- `pending_confirmation` + `row_type=data` + `row_action_status=pending_confirmation` + `buy_rank_eligible=False`: display only as pending confirmation; no entry price and no buy ranking.
- `active_operation` empty rows must use `row_action_status=empty_state` and `buy_rank_eligible=False` until a holding tracker exists.

## Sections

The CSV always includes these `pdf_section` values for both `pdf_view=highlight` and `pdf_view=full`:

- `confirmed_operation`: confirmed operation rows.
- `pending_confirmation`: pending signal rows.
- `active_operation`: operation-in-progress rows.

Until a real holding tracker exists, `active_operation` must contain `row_type=empty_state` rows with `stock_display=目前無資料`.

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
