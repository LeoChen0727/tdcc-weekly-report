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

## Future Quarterly Financial Statement Data Layer

The repository does not currently have a formal full-market quarterly or annual
financial statement history data layer equivalent to `monthly_revenue_history`.
Existing catalyst files may contain columns such as EPS or margin fields, but
they must not be treated as a complete point-in-time EPS, gross margin,
operating income, non-operating income, net income, or annual financial
statement history.

Future work should create a separate shared objective data family before any
model uses those fundamentals as gates, scores, ranking features, PDF metrics,
or promotion evidence. The expected scope is:

- quarterly and annual statement rows for all available listed and OTC stocks;
- point-in-time source availability date per filing or conservative source-date
  policy when exact filing timestamps are unavailable;
- EPS, gross margin, operating margin, operating income, non-operating income,
  net income, recurring/non-recurring flags where source data supports them;
- validated history artifacts, raw source retention, source-status artifacts,
  and freshness/fallback policy;
- registry entry in `config/daily_model_background_data_registry.csv`;
- validator and coverage audit before model-specific research matrices consume
  the data.

Until that data family exists, any `needs_eps_confirmation`,
`revenue_good_eps_unconfirmed`, EPS surprise, margin improvement, or
non-operating income interpretation remains disclosure/advisory context only
and must not be promoted into production model rules.

Revenue-model discussion trigger:

- Any future discussion of a revenue-driven model, revenue condition, or
  revenue interpretation must explicitly ask whether quarterly/annual financial
  statement fundamentals belong in scope.
- If the answer is yes, the next step is to design and build the formal
  financial-statement data layer before using those fields in backtest
  matrices, promotion decisions, model contracts, ranking, scoring, packets, or
  PDFs.
- If the answer is no, document that the current discussion is monthly-revenue
  only and do not use EPS, margin, operating/non-operating income, net income,
  or annual statement fields as implied evidence.

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
- `docs/latest/price_pullback_23ema_revenue_condition_matrix_latest.csv`
- `docs/latest/revenue_unreacted_range_revenue_condition_matrix_latest.csv`
- `docs/latest/revenue_unreacted_range_operation_candidate_matrix_latest.csv`
- `docs/latest/revenue_unreacted_range_feature_contrast_audit_latest.csv`
- `docs/latest/revenue_unreacted_range_feature_contrast_anomaly_audit_latest.csv`

The producer and validator are:

```text
python scripts/build_daily_model_parameter_research.py
python scripts/validate_daily_model_revenue_condition_matrix.py
python scripts/validate_revenue_unreacted_range_operation_candidate_matrix.py
python scripts/validate_revenue_unreacted_range_feature_contrast_audit.py
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

The anomaly audit publishes both including-known-anomaly and
excluding-known-revenue-and-price-anomaly bases. Only the excluding basis may be
interpreted, and it remains blocked if extreme-return dominance requires row-level
review. Revenue anomaly exclusion covers the current PIT row, the prior three
monthly YoY/cumulative YoY values used by the feature audit, and extreme one-month
delta values; a clean current row must not hide an anomalous lagged input. Sample
count is always reported but is not, by itself, a reason to reject a rare feature.

Large-detail policy: the row-level detail is tracked once at
`output/latest/research_backtest/revenue_unreacted_range_feature_contrast_audit_detail_latest.csv`.
It is not duplicated under `docs/latest` or `output/history`; Git history plus the
summary/anomaly history mirrors preserve audit lineage without tripling the large
CSV on every refresh.

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
price is the next trading day open. The main promotion-matrix statistics must
use `excluding_known_data_quality_exceptions` or the revenue equivalent
`excluding_known_price_or_revenue_anomalies`; including-anomaly rows are audit
comparisons only and cannot be cited as promotion evidence. Continuation variants such as
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
