# Daily Volume Breakout Operation Section Contract

This contract is the handoff from production/model code to the PDF/packet renderer.

The PDF renderer must read:

- `output/latest/daily_volume_breakout_operation_section_latest.csv`
- `output/latest/daily_volume_breakout_operation_section_latest.md`

The adapter also emits an audit-only artifact:

- `output/latest/daily_volume_breakout_operation_evidence_audit_latest.csv`
- `output/latest/daily_volume_breakout_operation_evidence_audit_latest.md`

This audit explains why confirmed/active candidates were included or excluded. It is not a PDF source.
It must also record source gaps for lifecycle candidates that cannot be evaluated
because stock price history is missing the signal date, as-of date, or required
price fields. Source-gap rows are audit-only and must never be rendered as daily
operation rows.
It must also record same-stock lifecycle suppression when only one operation row
can be rendered for a stock. Suppressed rows are audit-only, must carry
`audit_status=lifecycle_suppressed`, and must never be rendered as daily
operation rows.

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
- `output/history/daily_candidate_models/daily_candidate_model_signal_log.csv`
- `output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv`
- `data/stock_price_history/{stock_id}.csv`
- `config/approved_operation_evidence/volume_breakout_operation_v1_20260615_formal_operation_backtest.csv`
- `output/latest/approved_operation_patterns_latest.csv`

Research/backtest may also emit `output/latest/volume_breakout_formal_operation_lifecycle_latest.csv`
to audit `pending_confirmation`, `confirmed_operation`, `active_operation`, and `expired`
states. That lifecycle artifact is not a PDF or daily adapter source.

## Scope

- `model_id` is always `volume_range_breakout`.
- The artifact is a production operation adapter, not a PDF calculation layer and not a research/backtest runner.
- It must not run backtests inside `daily_full_pipeline.yml`.
- `config/approved_operation_evidence/volume_breakout_operation_v1_20260615_formal_operation_backtest.csv` is the only approved v1 operation evidence source for daily confirmed/active guidance.
- The approved v1 evidence source is versioned and immutable. Later research/backtest latest artifacts may support a future promotion, but they must not silently change the approved v1 daily adapter.
- Published report-date operation snapshots under `output/history/daily_model_snapshots/` are immutable as-published evidence. A same-date rewrite is allowed only for an explicit correction run with `ALLOW_DAILY_MODEL_SNAPSHOT_REWRITE=1`; ordinary daily rebuilds must fail closed or reuse the already published snapshot.
- Its win rate, average return, and median return must be computed only from `metric_sample_scope=mature_selected_operation_only` rows.
- Missing or empty formal operation evidence must fail validation; the PDF must not fabricate buy/stop/exit rows.
- Other stock models must not reuse this operation section, ranking, entry rule, stop rule, or exit rule.
- `approved_for_daily=True` means this adapter is allowed to present `volume_range_breakout` v1 operation guidance. It does not approve any other model.
- `approved_for_daily=True` is module-level approval, not row-level buy permission.
- The PDF renderer must use `buy_rank_eligible=True` plus `row_action_status=confirmed_buy_candidate` for buy-ranking rows.
- `pending_confirmation` rows must remain `buy_rank_eligible=False` even when `approved_for_daily=True`.
- The adapter must copy approval metadata from `approved_operation_patterns_latest.csv`; the PDF renderer must not read that approval table directly.
- `confirmed_operation` data rows must be positive formal evidence only. The matched evidence row itself must carry `approved_for_daily=True` and must not be marked `research only` in `risk_notes_zh`. Module-level approval in `approved_operation_patterns_latest.csv` is not enough to make a row buyable.
- Evidence rows with `approved_for_daily=False`, missing row-level approval, or `risk_notes_zh` marked `research only` may remain audit / research context only. They must not enter `confirmed_operation` or `active_operation`.
- Weak-evidence or research-only confirmations must not be presented as daily buy guidance.
- `confirmed_unranked_operation` data rows are lifecycle-confirmed rows that did not pass the buy-ranking evidence gate. They must remain `buy_rank_eligible=False`, must not carry entry price, stop price, or exit guidance, and must be rendered only in full PDFs.
- `active_operation` data rows must trace back to a confirmation-date published `confirmed_operation` row with `row_action_status=confirmed_buy_candidate` and `buy_rank_eligible=True`, and the current row-level evidence gate must still pass formal approval. A prior `active_operation` snapshot is not sufficient by itself; it may continue tracking only when the original confirmation snapshot remains buy-ranked and the matched evidence row remains formal-approved.
- `confirmed_operation`, `confirmed_unranked_operation`, and `active_operation` data rows must use row-level evidence attribution when matching evidence exists. The adapter must match the selected trigger plus that stock's TDCC list type, rank bucket, and best available confluence row before copying sample size, win rate, average return, or median return.
- If no positive formal row-level evidence exists for a confirmation on the report date, the adapter must keep the lifecycle-confirmed row in `confirmed_unranked_operation` instead of dropping it from the full report. It must not enter `active_operation`.
- If a lifecycle source signal cannot be evaluated because stock price history is
  missing or incomplete, the adapter must emit `audit_status=source_gap` in
  `daily_volume_breakout_operation_evidence_audit_latest.csv`, keep
  `included_in_daily_adapter=False`, and emit no operation data row for that
  signal.
- If multiple lifecycle records exist for the same stock, the adapter may render
  only the highest-priority lifecycle row for that stock. Every lower-priority or
  later same-priority suppressed record must emit `audit_status=lifecycle_suppressed`,
  keep `included_in_daily_adapter=False`, and preserve its own `stock_id`,
  `signal_date`, `operation_asof_date`, and lifecycle state in the audit.
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
- `operation_status`
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

- `operation_status` is the machine-readable lifecycle section. It must mirror `pdf_section` exactly so downstream renderers and audits do not infer lifecycle state from Chinese display text.
- `confirmed_operation` + `row_type=data` + `row_action_status=confirmed_buy_candidate` + `buy_rank_eligible=True`: eligible for the daily buy ranking table.
- `confirmed_unranked_operation` + `row_type=data` + `row_action_status=confirmed_not_buy_ranked` + `buy_rank_eligible=False`: confirmed by lifecycle, but not eligible for the daily buy ranking table.
- `pending_confirmation` + `row_type=data` + `row_action_status=pending_confirmation` + `buy_rank_eligible=False`: display only as pending confirmation; no entry price and no buy ranking.
- `active_operation` + `row_type=data` + `row_action_status=active_operation` + `buy_rank_eligible=False`: already entered tracking from an earlier confirmed row; it is not a new buy ranking row.
- `empty_state` rows must use `row_action_status=empty_state` and `buy_rank_eligible=False`.

Operation field meaning:

- `final_rank_score` is the daily production ranking score for `volume_range_breakout`; PDF must render it and must not recalculate it.
- `operation_score`, `tdcc_score`, `pattern_score`, and `risk_penalty` are score components copied from the daily model layer for auditability.
- `entry_rule_id=confirmation_next_open` means a confirmed row uses the next trading day's open after the selected confirmation date.
- `entry_date` and `entry_price` are structured entry fields. They stay blank on `confirmed_operation` until the next trading day's open exists, are required on `active_operation` data rows, and must remain blank on `confirmed_unranked_operation` and `pending_confirmation`.
- `stop_loss_rule_id=signal_low_stop` means the stop basis is the signal-date low, displayed as `{M/D}最低點`.
- `exit_rule_id=signal_low_stop_or_fixed_10d_close` means exit at the stop first, otherwise fixed 10 trading-day close.
- `pending_confirmation` rows must not show an entry price; they may carry rule IDs only to describe the eventual rule after confirmation.

## Sections

The CSV always includes these `pdf_section` values for both `pdf_view=highlight` and `pdf_view=full`:

- `confirmed_operation`: confirmed operation rows.
- `confirmed_unranked_operation`: lifecycle-confirmed rows that did not pass the buy-ranking evidence gate; full PDF only.
- `pending_confirmation`: pending signal rows.
- `active_operation`: operation-in-progress rows.

`pdf_view=highlight` must include only `confirmed_operation` and `active_operation`.
It must not emit `pending_confirmation` or `confirmed_unranked_operation` rows, not even empty-state rows.
`pdf_view=full` may include all four sections. A section may use `row_type=empty_state` only when that section has no data rows.

PDF display limits:

- `pdf_view=highlight` must render at most 10 `confirmed_operation` data rows and at most 5 `active_operation` data rows after mainstream / non-mainstream report-line filtering. It must not render `pending_confirmation` or `confirmed_unranked_operation`.
- `pdf_view=full` must not apply these highlight limits; it should render all valid operation rows for the selected report line.
- These limits are presentation limits only. They must not change row lifecycle state, `buy_rank_eligible`, trigger evidence, model scores, or model ranks. The adapter encodes which sections are visible in each `pdf_view`.

Lifecycle meaning:

- First daily model hit enters `pending_confirmation`.
- If a later trading day meets one confirmation trigger before invalidation, it enters `confirmed_operation` only on that confirmation report date when row-level evidence passes the formal buy-ranking gate; otherwise it enters `confirmed_unranked_operation` on that confirmation report date.
- After the entry day starts, it enters `active_operation` until stop or the 10th trading-day holding limit only if the confirmation-date published operation snapshot contains the same stock/signal as `confirmed_operation` with `row_action_status=confirmed_buy_candidate` and `buy_rank_eligible=True`, and the matched row-level evidence still passes the formal buy-ranking gate.
- A row that was `confirmed_unranked_operation` on its confirmation date must remain not-tracked for active operation purposes. Later TDCC, context, or evidence changes must not re-promote that historical signal into `active_operation`.
- If a signal breaks its stop basis before confirmation, exceeds the confirmation window, hits stop after entry, or exceeds the holding window, it must drop from the operation section. A row that confirms without buy-ranking evidence must not be tracked as active.

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

## Volume V2 操作管理欄位與當日停損提醒（2026-11-01）

本節只適用於 `volume_range_breakout_v2_low_position_volume_attack`、
`volume_range_breakout_v2_mid_position_momentum_attack` 與
`volume_range_breakout_v2_high_position_volume_attack`。三者仍使用各自核准的條件、
排序及統計；本節不沿用上方 legacy v1 的 10 日或訊號低點停損規則。

三個 V2 的既有契約為：確認日收盤成立後下一交易日開盤入場；從實際入場日開始，
每日以 `close <= 0.96 * min(valid positive MA20, EMA23)` 計數，不成立即歸零。
連續第 4 日收盤確認後，下一交易日開盤停損；未提前停損則入場日計第 1 日、
第 15 個股票交易價格列收盤出場。第 14 日首次達第 4 次時在第 15 日開盤停損；
首次第 4 次落在第 15 日時，維持已核准的第 15 日固定收盤出場，不新增第 16 日退出。
MA20／EMA23 的來源、精度、缺值處理及價格比較子均維持既有 V2 規則。

正式 adapter 新增以下欄位；renderer 只讀取，不重新計算：

- `stop_reference_price`、`stop_reference_date`：資料日的動態收盤停損參考線及其日期。
  參考線不是成交價，也不是入場價固定扣 4%；不能固定沿用於未來交易日。
  依既有規則兩條均線都不可用時，參考價留空、當期計數歸零，不補 0 或宣稱已確認停損。
- `stop_confirmed_days`：從該筆實際入場日開始的當期連續符合日數。
- `holding_days`：實際入場日為 1 的持有交易列數；V2 的 `operation_age_days`
  同步採此口徑，不能再從訊號日或確認日起算。
- `planned_entry_date`：確認候選的排定入場日期；既有 active 可保留相同實際入場日期。
- `planned_exit_date`、`planned_exit_date_status`：未提前停損情境的排定 D15 收盤日期與狀態。
- `next_action_date`、`next_action_date_status`：只供已確認停損、等待下一開盤的列使用。
- `stop_confirmation_date`、`next_action_zh`：已成立的收盤確認日期與面向使用者的下一動作。

尚未入場的 confirmed 列，其 `holding_days`、`stop_confirmed_days` 保持空白或 0，
原 `entry_date`、`entry_price` 不填預估值。pending、confirmed-unranked 與 empty-state
不得取得操作管理價格或排定買賣日期；不得因補欄位而升級為已買入或 active。

第 4 日收盤已成立、但當時尚無下一筆價格列時，adapter 必須保留當期正式追蹤列，
以 `row_action_status=stop_exit_pending_next_open` 明示等待下一開盤停損。
其 `pdf_section`、`operation_status` 仍為 `active_operation`，`operation_status_zh`
仍為 `操作中`、`quality_status_zh` 仍為 `已進場追蹤`，且 `buy_rank_eligible=False`。
不得重複寫入 protected fields，亦不得新增已出場主 section。實際下一開盤資料存在且
已在 as-of 範圍內時，才可形成已實際退出的 audit 欄位；pending 不填實際出場價。

排定日期只讀取既存 `output/latest/market_session_status_latest.json`：年度官方來源
`official_sources.twse_annual_calendar.status=ok`、有效 SHA-256、`covered_years`，
加上其中 `scheduled_non_trading_days` 與 `exceptional_non_trading_days`。不 fetch、
不新增行情、不建立另一個年曆 producer。來源缺失、無效或日期年份未涵蓋時，該日期留空，
對應狀態為 `unavailable_calendar`；可排定時使用 `scheduled_official_calendar`。
排定不代表未來已開市、個股有可用開盤價或券商已成交；實際日期改變須依原規則重新核算。

既存年曆的單一 writer、精確 artifact 路徑、三個 V2 read-only consumers、latest-only
限制及禁止歷史 PIT／績效／promotion 用途，登錄於
`config/daily_model_background_data_registry.csv` 與
`config/daily_model_data_sharing_registry.csv`，並由
`config/daily_model_data_sharing_migrations.csv` 的
`volume_v2_existing_official_calendar_consumer_20261101` 追加核准。

model validator 必須拒絕錯誤參考日期、負數／非整數計數、仍以訊號日起算的持有日數、
第 4 次卻沒有 pending-stop action、未滿 4 次卻顯示 pending-stop、錯誤排定日期、
缺年曆卻有日期、以及把尚未發生的開盤填成實際退出。三個 V2 的非空 active 與 pending-stop
builder rows 都必須通過 model validator 與 protected-field validator。
