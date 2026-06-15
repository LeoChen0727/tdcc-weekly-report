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
- The adapter must copy approval metadata from `approved_operation_patterns_latest.csv`; the PDF renderer must not read that approval table directly.
- `confirmed_operation` data rows must be positive evidence only. Weak-evidence confirmed rows from research previews must not be presented as daily buy guidance.

## Required Approval Fields

The CSV must include these approval fields on every row:

- `approval_source`
- `approved_for_daily`
- `approval_status`
- `operation_module_id`
- `approval_version`
- `operation_directive_level`
- `buy_filter_id`
- `approval_note_zh`

For the approved v1 daily adapter, these fields must show:

- `approved_for_daily=True`
- `approval_status=approved_for_daily_v1`
- `operation_directive_level=approved_daily_operation_guidance`

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
