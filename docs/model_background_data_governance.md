# Daily Model Background Data Governance

This document defines the boundary between shared background data and
model-specific interpretation for daily stock model research.

## Rule

Shared background data may contain only objective point-in-time facts or
measurements. Examples include OHLCV history, TDCC holder-flow ratios, market
index returns, and raw 20/45/90-day price-window metrics computed on or before
`signal_date`.

Model-specific interpretation must stay outside shared data families. Examples:

- `neckline_context_*` is owned by `neckline_volume_breakout_confirmation`.
- `w_bottom_*` geometry and path-quality fields are owned by W-bottom model
  families.
- `price_pullback_23ema_*` research outputs are owned by `price_pullback_23ema`.

The shared 45/90-day numeric features can be reused. The neckline 45-day
non-bearish filter cannot be reused as a 23EMA rule.

## Registry

The contract table is:

`config/daily_model_background_data_registry.csv`

Each row is a data family, not a single column. Important fields:

- `scope`: shared objective data, replay evidence, latest-only context,
  model-specific interpretation, model research output, or a missing shared
  data family.
- `consumer_models`: `all_models` is allowed only for shared objective/replay
  data, never for model-specific interpretation.
- `point_in_time_status`: whether the family can be used safely for historical
  signal dates.
- `allowed_use` / `forbidden_use`: the operational boundary.
- `cleanup_status`: whether the data is active, blocked, or a deletion review
  candidate.

The validator is:

`python scripts/validate_daily_model_background_data_registry.py`

## Cleanup Audit

Before deleting or relocating a registered data family, run:

```text
python scripts/build_daily_model_background_data_cleanup_audit.py
python scripts/validate_daily_model_background_data_cleanup_audit.py
```

The audit artifacts are:

- `output/latest/research_backtest/daily_model_background_data_cleanup_audit_latest.csv`
- `output/latest/research_backtest/daily_model_background_data_cleanup_audit_latest.md`
- `docs/latest/daily_model_background_data_cleanup_audit_latest.csv`
- `docs/latest/daily_model_background_data_cleanup_audit_latest.md`

These files are a deletion gate, not deletion approval. A row can become a
cleanup PR candidate only when `cleanup_status=deprecated_candidate` and the
audit finds no active workflow, inventory, lineage, validator, replay, parity,
or promotion dependency.

## Cleanup Policy

Do not delete research, history, or latest artifacts just because they look
old. A data family can be deleted only after a separate cleanup PR proves:

1. No active workflow consumes it.
2. No validator or report/packet consumer depends on it.
3. It is not historical replay evidence.
4. It is not required for model parity, readiness, or promotion audit trail.
5. The registry marks it `deprecated_candidate`.
6. The cleanup audit marks `deletion_allowed=True`.

This PR intentionally lists cleanup boundaries but does not delete historical
snapshots or model research evidence.

## Monthly Revenue History

Monthly revenue now has a full-market source history data layer:

- `data/monthly_revenue_history/monthly_revenue_history.csv`
- `data/monthly_revenue_history/raw/*.csv`
- `data/monthly_revenue_history/raw/mops_html/*.html`
- `output/latest/research_backtest/monthly_revenue_history_latest.csv`
- `docs/latest/monthly_revenue_history_latest.csv`

The producer and validator are:

```text
python scripts/build_monthly_revenue_history.py
python scripts/backfill_monthly_revenue_history_from_mops_html.py
python scripts/validate_monthly_revenue_history.py
```

Allowed use: save official TWSE / TPEX monthly revenue rows for all returned
listed and OTC securities, and join research rows where `source_table_date <=
signal_date`.

Forbidden use: do not label older historical signals with the latest saved
revenue period. The current official OpenAPI returns the latest available
monthly revenue period only, so older periods are filled only by the validated
historical backfill builder. The historical MOPS static HTML backfill uses
`source_table_date_raw=conservative_next_month_17th`; this intentionally delays
availability to avoid lookahead when exact original filing timestamps are not
present in the static HTML page. Formal model gates still require a sufficient
coverage audit and model promotion approval.

This data family is the canonical revenue source to build on. Do not replace it
with current/latest candidate artifacts, PDF outputs, or model-specific revenue
interpretations.

Current validated historical backfill coverage:

- `revenue_period_min=202405`
- `revenue_period_max=202605`
- `history_revenue_period_count=25`
- source: official MOPS static monthly revenue HTML under
  `https://mopsov.twse.com.tw/nas/t21/{sii,otc}/...`
- source-date policy: conservative next-month-17 availability, not the static
  page display date.

Monthly revenue official-source fallback policy:

- The pipeline must try official TWSE / TPEX sources first.
- If official sources are temporarily empty, unavailable, or incomplete, the
  builder may reuse the latest validated full-market monthly revenue history
  cache.
- The cache may be reused for at most 25 days from its latest
  `source_table_date`.
- A stale cache must fail closed instead of silently treating old revenue data
  as current.

## Quarterly Financial Statement Point-In-Time Data Layer

The repository now has an independent shared-objective financial-statement PIT
governance skeleton. Its currently published data is a 2026 Q1 snapshot, not a
completed historical PIT series. It is separate from monthly revenue and from
every model-owned research producer:

- `data/financial_statement_history/financial_statement_history.csv`
- `data/financial_statement_history/financial_statement_source_manifest.csv`
- `output/latest/research_backtest/financial_statement_pit_coverage_latest.csv`
- `docs/latest/financial_statement_pit_coverage_latest.csv`

The producer and independent validator are:

```text
python scripts/build_financial_statement_pit.py --fetch-current --raw-archive-dir <external-directory>
python scripts/validate_financial_statement_pit.py
```

Historical source qualification is a separate fail-closed gate:

```text
python scripts/build_financial_statement_historical_pit_source_audit.py
python scripts/validate_financial_statement_historical_pit_source_audit.py
```

The committed pilot uses `2013Q1` as the earliest IFRS source-contract probe and
`2025Q1` as the first modern quarter near the currently tracked price-history
window. The tracked pilot stocks currently begin at `2025-04-07`; therefore
2013-2024 source retention is not current backtest evidence. Official MOPS bulk
ZIPs, single-company downloads, financial-report announcements, correction
queries, and taxonomy packages prove payload, scope, industry, and correction
event coverage, but not exact initial `filed_at` plus every prior revision
payload. `ReviewAuditDate`, ZIP member times, statutory deadlines, and local
first-observed times must not be substituted for filing availability.

Until that source blocker is resolved, `pit_eligible=False` and
`formal_model_use_allowed=False` remain mandatory. EPS, gross margin, operating
margin, operating income, non-operating income, and net income must not enter
`revenue_unreacted_range`, production gates, scores, rankings, PDFs, packets,
or promotion evidence.

The source and metric contracts are:

- `config/daily_model_financial_statement_pit_sources.csv`
- `config/daily_model_financial_statement_metric_mapping.csv`

The current source layer consumes twelve official TWSE / TPEx income-statement
OpenAPI endpoints: listed and OTC markets crossed with general, banking,
securities, financial holding, insurance, and other schemas. It preserves the
industry schema instead of forcing financial-company statements into the
general-industry formula set.

Current validated snapshot coverage is 2026 Q1: twelve captured sources, 1,972
raw rows, 1,968 normalized company rows, and four TPEx blank placeholder rows.
EPS and net-income fields are present on every normalized row. Gross margin,
operating margin, and net margin are derived only for the general schema from
cumulative reported values; they remain blank for financial and other schemas.
Quarterly income-statement values remain `cumulative_ytd`. Standalone quarterly
EPS must not be derived by subtracting cumulative EPS.

The current snapshot has 36 numerical anomaly candidates triggered only by
large EPS or absolute margin thresholds. They remain in primary data with
`anomaly_disposition=unresolved_anomaly_candidate`. The source payload and
formula lineage are recorded, but independent corroboration and complete
root-cause disposition are still required. A threshold cannot classify a row as
a data error or justify exclusion.

Point-in-time boundary:

- The current OpenAPI global table date is not a company filing date.
- Current rows use `first_observed_at` as their earliest safe availability and
  have `pit_status=current_snapshot_first_observed_only`.
- Every source payload and row is bound to SHA-256. Raw JSON and future XBRL
  archives remain outside the repository in a content-addressed archive.
- Revisions are append-only. A new filing version receives a new `revision_id`
  and links to the prior version through `supersedes_revision_id`; old versions
  are not overwritten.
- `allowed_for_formal_model_use=False` is mandatory in this data-layer scope.
- `--capture-manifest` may replay payloads only under their registered source
  contract. A current OpenAPI source cannot self-declare
  `historical_pit_eligible=True`; a future historical source requires its own
  registry entry, exact filing-availability semantics, parser, validator, and
  user-approved data-sharing migration.

Allowed use: objective research-only as-of joins where
`source_available_at <= signal_date` and the row's industry schema supports the
requested field.

Forbidden use: EPS, gross margin, operating margin, operating income,
non-operating income, net income, or annual-statement fields must not become a
production gate, score, ranking rule, packet field, PDF metric, or promotion
evidence from the current snapshot layer.

Remaining historical PIT work:

1. Ingest official MOPS/XBRL filing history with exact company filing
   availability and explicit consolidated or individual statement scope.
2. Cover the IFRS-comparable listed and OTC baseline from 2013 Q1 forward and
   preserve every later revision.
3. Validate fiscal-period continuity, units, formulas, statement scope, and
   market / industry / quarter coverage.
4. Keep raw archives external and content-addressed while retaining immutable
   source manifest hashes in the repository.
5. Open a separate model-specific research and promotion decision before any
   financial field is used formally.

Revenue-model discussion trigger remains mandatory. Monthly revenue and
quarterly or annual financial statements must always be named separately. A
monthly-revenue conclusion cannot imply EPS, margin, operating income,
non-operating income, or net-income evidence.

## Monthly Revenue Coverage / Backfill Audit

Monthly revenue coverage is audited by:

```text
python scripts/build_monthly_revenue_coverage_backfill_audit.py
python scripts/validate_monthly_revenue_coverage_backfill_audit.py
```

The latest artifacts are:

- `output/latest/research_backtest/monthly_revenue_coverage_backfill_audit_latest.csv`
- `output/latest/research_backtest/monthly_revenue_coverage_backfill_audit_detail_latest.csv`
- `output/latest/research_backtest/monthly_revenue_coverage_backfill_audit_latest.md`
- `docs/latest/monthly_revenue_coverage_backfill_audit_latest.csv`
- `docs/latest/monthly_revenue_coverage_backfill_audit_latest.md`

The audit measures whether canonical full-market monthly revenue rows can be
joined point-in-time by `source_table_date <= signal_date`, including model-level
coverage for `price_pullback_23ema` and `revenue_unreacted_range`.

Formal revenue gates remain blocked unless the audit reports enough history
months and enough signal-row / stock coverage. A candidate snapshot PIT panel is
not a validated full-market historical backfill source.

## Revenue Condition Matrices

Model-specific revenue condition matrices are research interpretation evidence,
not shared objective background data:

- `output/latest/research_backtest/price_pullback_23ema_revenue_condition_matrix_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_revenue_condition_matrix_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_operation_candidate_matrix_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_feature_contrast_audit_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_feature_contrast_audit_detail_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_feature_contrast_anomaly_audit_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_close_confirmation_timing_audit_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_close_confirmation_timing_audit_detail_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_close_confirmation_timing_audit_anomaly_audit_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv`
- `output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_anomaly_audit_latest.csv`
- `docs/latest/price_pullback_23ema_revenue_condition_matrix_latest.csv`
- `docs/latest/revenue_unreacted_range_revenue_condition_matrix_latest.csv`
- `docs/latest/revenue_unreacted_range_operation_candidate_matrix_latest.csv`
- `docs/latest/revenue_unreacted_range_feature_contrast_audit_latest.csv`
- `docs/latest/revenue_unreacted_range_feature_contrast_anomaly_audit_latest.csv`
- `docs/latest/revenue_unreacted_range_close_confirmation_timing_audit_latest.csv`
- `docs/latest/revenue_unreacted_range_close_confirmation_timing_audit_anomaly_audit_latest.csv`
- `docs/latest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_latest.csv`
- `docs/latest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_anomaly_audit_latest.csv`

The producer and validator are:

```text
python scripts/build_daily_model_parameter_research.py
python scripts/validate_daily_model_revenue_condition_matrix.py
python scripts/validate_revenue_unreacted_range_operation_candidate_matrix.py
python scripts/validate_revenue_unreacted_range_feature_contrast_audit.py
python scripts/validate_revenue_unreacted_range_close_confirmation_timing_audit.py
python scripts/validate_revenue_unreacted_range_fixed_confirmation_feature_contrast.py
```

Allowed use: compare model-specific revenue conditions under the matrix's stated
buy point, sell rule, stop rule, anomaly-exclusion basis, same-stock non-overlap
basis, and `source_table_date <= signal_date` monthly revenue join.

Forbidden use: do not use these matrix rows as production gates, scores,
rankings, PDF metrics, or shared cross-model features. `monthly_revenue_history`
is the reusable objective input; the matrix conclusion is specific to the named
model and still needs an explicit promotion PR before formal use.

The `revenue_unreacted_range_feature_contrast_audit` family fixes one common
operation basis before comparing high-return and failure samples: strong monthly
revenue, signal-date close confirmation, next-trading-day open entry, D+20 close
exit, no stop, and a 20-trading-day same-stock non-overlap rule. Its summary rows
must publish each binary feature's prevalence in both the high-return and failure
groups and must recompute the selected subset's true win, neutral, failure,
average-return, median-return, high-return, and large-loss metrics. Single-feature
results are not combination evidence. Future combinations must be recomputed on
the actual intersection and rejected when they perform worse than the best
applicable single feature.

The anomaly audit publishes a primary basis that retains every unresolved
anomaly candidate and a separately labeled candidate-exclusion sensitivity
basis. Only the primary basis is the model result; the sensitivity basis cannot
replace or be described as corrected performance. Threshold checks cover the
current PIT row, the prior three monthly YoY/cumulative YoY values used by the
feature audit, and large one-month delta values so a clean current row cannot
hide a lagged candidate. Any unresolved candidate blocks promotion. Sample count
is always reported but is not, by itself, a reason to reject a rare feature.

Large-detail policy: the row-level detail is tracked once at
`output/latest/research_backtest/revenue_unreacted_range_feature_contrast_audit_detail_latest.csv`.
It is not duplicated under `docs/latest` or `output/history`; Git history plus the
summary/anomaly history mirrors preserve audit lineage without tripling the large
CSV on every refresh.

The `revenue_unreacted_range_close_confirmation_timing_audit` family starts
from the same point-in-time strong-revenue and recent-range candidate source,
but it does not treat that source as a buyable model. It independently replays
three Chinese research branches: `隔日續強確認型`, `區間突破確認型`, and
`均線站回確認型`. Candidate date close enters pending status; every confirmation
is known at a close and entry is the next trading day open. The audit compares
the original signal-relative D+20 close with a confirmation-relative D+20 close
without a stop so confirmation timing is isolated before stop research.

Every branch has its own chronological same-stock pending/active lifecycle.
Source signals must be fully accounted for as one episode or a suppressed row,
same-stock accepted overlap must remain zero, and branch performance must never
be pooled. The source-partition rows report exact overlap among the three
confirmation branches so a future model-split decision cannot hide unclassified
signals. Win, neutral, and failure remain `>= +5%`, `0% to < +5%`, and `< 0%`.
Sample count is disclosed but is not a rejection rule by itself.

The timing detail keeps only confirmed mature trades and price-path anomaly-candidate
evidence. Unconfirmed, not-evaluable, avoided-failure, missed-win, and source
accounting totals remain complete in the summary. The compact detail is tracked
once under `output/latest/research_backtest`; it is not copied to `docs/latest`
or `output/history`. All rows remain research-only and require a separate model
promotion PR before any production gate, score, ranking, operation adapter, or
PDF metric use.

The `revenue_unreacted_range_fixed_confirmation_feature_contrast_audit` family
fixes one timing branch before interpreting features:
`range23_highest_close_breakout`, at most three trading days pending,
confirmation-close information only, next-trading-day open entry, and
`confirmation_d20_close` with no stop. It publishes signal-date-close and
confirmation-date-close feature contexts separately. A feature known only at
confirmation must never be relabeled as signal-date evidence.

The artifact compares monthly-revenue strength, price position/shape, TDCC,
technical indicators, and market regime in high-return, win, and failure groups.
Every binary feature must expose observed coverage, high-return and failure hit
rates within observed rows, and the selected subset's recomputed win/neutral/
failure/average/median/high-return/large-loss metrics. It tests single features
only; combinations require a separate exact-intersection recomputation and may
not reuse single-feature metrics.

Decision rows must have zero same-stock operation overlap and zero repeated
`stock_id + source_monthly_revenue_period` trades. An `|return| >= 80%` cutoff
creates only an anomaly candidate and a threshold-exclusion sensitivity view.
It does not classify an extreme value and cannot produce corrected performance.
The current raw-OHLC replay is only a partial root-cause check because the repo
does not yet provide complete historical corporate-action PIT coverage or an
independent authoritative price-source confirmation for every row. Such rows
remain `unresolved_anomaly_candidate`, stay in the primary basis, and block
promotion conclusions until every root-cause check in
`config/daily_model_numerical_anomaly_disposition_contract.csv` is complete.

All rolling price-structure and volume windows used by this research producer
must be isolated by `stock_id`. A shifted Series must not be rolled globally
across stock boundaries. Regression coverage must use stocks with materially
different price and volume scales and prove that 10/20/23/30/45/60/120-day
high/low windows and volume MA20 consume only the same stock's earlier rows.

Monthly-revenue anomaly candidates are evaluated again at each feature context
date, not only on the original signal row. A legacy
`full_monthly_revenue_numerical_anomaly_flag` is a threshold-generated candidate
only. Until root-cause disposition is complete, the trade and its observed
monthly-revenue values remain in the primary binary and numeric feature evidence.
Candidate counts must be published in the summary and anomaly audit; any
candidate-excluded feature result must be a separately named sensitivity view.

This artifact uses point-in-time monthly revenue only. Quarterly/annual
financial statements, EPS, gross margin, operating margin, operating income,
non-operating income, and net income remain excluded until a formal shared
point-in-time financial-statement data layer exists and passes coverage
validation. All outputs remain research-only and cannot become a production
gate, score, ranking, operation adapter, or PDF metric without a separate
promotion PR.

## Volume Breakout V2 High-Position Improvement Audit

`volume_range_breakout_v2_high_position_improvement_audit_latest.csv` is a
model-specific research-only artifact for the high-position volume attack future
model discussion. It consumes the existing v2 position-shape matrix detail and
raw-market rerun detail, then compares TDCC, market-regime, previous-60-day
shape, and technical features under the same close-only operation basis.
The audit keeps the pre-filter universe
`high_pos_gt75_non_consolidation_or_wide` only as `reference_universe`; the
research baseline is
`high_pos_gt75_nonconsolidation_or_wide_ma60_gt_ma120`. `mild_bull`,
TDCC, breakout-size, EMA23-distance, volume, signal-body, close-location, and
confirmation-return rows are add-score or risk-filter diagnostics only. The
artifact also computes signal-date KDJ from stock-local price history. New
discussion and new artifacts must treat `kdj_*` columns as the authoritative
KDJ display fields; existing `kd_*` columns are legacy compatibility aliases and
must not be described to users as a KD-only test when `kd_j_signal` /
`kdj_j_signal` is present. The artifact emits both add-score overlap diagnostics
and exact PDF add-score combo rows (`row_type=pdf_bonus_combo`,
`feature_family=pdf_bonus_combo`). An exact combo row recalculates
win/neutral/loss rates and average/median return for the actual feature set
matched by a stock, such as
`pdf_combo__breakout_2_5__signal_body_le3`, instead of reusing the whole-model
baseline or an individual add-score row.

PDF-facing use: if a future daily operation adapter exposes row-level add-score
combo performance fields, the PDF table's performance columns must display the
matched exact combo metric for that row. The whole-model baseline may appear in
header, summary, or audit context only; it must not be shown inside a stock row
that is already labeled with a stronger add-score combo. Renderer implementation
belongs to the daily PDF layout lane after this contract is promoted.

Allowed use: discuss whether high-position volume attack needs an add-score,
risk tag, or future model-specific condition after comparing both win and loss
feature shares.

Forbidden use: do not use the audit as a hidden production gate, daily ranking
rule, PDF metric, operation adapter, or promotion evidence without a dedicated
model decision and promotion PR.

## Price Pullback 23EMA Promotion Matrix

`price_pullback_23ema_promotion_matrix_latest.csv` is a research-only decision
matrix for the 23EMA model discussion. It gathers evidence from lifecycle replay,
ordered condition tests, high-return structure score buckets, and model-specific
revenue condition matrices into candidate roles such as required gate package,
add-score package, risk tag, rejected condition, or deferred context.

The producer and validator are:

```text
python scripts/build_daily_model_parameter_research.py
python scripts/validate_price_pullback_promotion_matrix.py
```

Allowed use: discuss which 23EMA conditions should become necessary conditions,
score items, risk tags, or rejected/deferred items under the same buy point, sell
rule, lifecycle suppression, and anomaly-exclusion basis.

Current approved discussion basis: `close_prev20_high_break_next_open`, meaning
the signal is close-confirmed, entry is the next trading day open, exit is only
after the close breaks the signal-day previous 20-day high, and the realized exit
price is the next trading day open. Primary promotion-matrix statistics must
retain every unresolved numerical anomaly candidate. A candidate-excluded basis
is sensitivity analysis only and cannot replace primary performance. The model
promotion conclusion remains blocked until each candidate receives a complete
root-cause disposition under
`config/daily_model_numerical_anomaly_disposition_contract.csv`. Continuation variants such as
`close_prev20_break_then_tp5_or_5ma_next_open`,
`close_prev20_break_then_tp8_or_5ma_next_open`, and
`close_prev20_break_then_tp10_or_5ma_next_open` remain research-only comparison
artifacts and must not be used as the promotion-matrix basis unless the user
explicitly reopens and approves a new sell-rule decision.

Forbidden use: do not use promotion-matrix rows as production gates, scores,
rankings, PDF metrics, operation rows, or contract approval. Formal use still
requires an explicit model promotion PR, parity/contract updates, validators,
merge to `main`, post-merge main validation, and a model-owned PDF operation
metric/adapter contract where presentation is affected.

## Revenue PIT Panel

Monthly revenue now has a coverage-limited point-in-time panel:

- `output/latest/research_backtest/monthly_revenue_point_in_time_panel_latest.csv`
- `docs/latest/monthly_revenue_point_in_time_panel_latest.csv`
- `output/history/research/monthly_revenue_point_in_time_panel.csv`

The producer and validator are:

```text
python scripts/build_monthly_revenue_point_in_time_panel.py
python scripts/validate_monthly_revenue_point_in_time_panel.py
```

Allowed use: research-only as-of joins where `research_join_allowed=True` and
`observed_as_of_date <= signal_date`.

Forbidden use: do not treat this panel as a formal historical revenue gate or a
production scoring/ranking rule. It is built from revenue values observed in
daily all-candidates snapshots, and the actual per-company release date is still
incomplete when the source field contains only a revenue year-month such as
`11505`.

Promotion requirement: formal revenue gates still require a fuller validated
release-date source or a model-specific promotion PR that explicitly accepts the
coverage limitation.
