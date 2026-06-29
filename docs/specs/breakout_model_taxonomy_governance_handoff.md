# Breakout Model Taxonomy Governance Handoff

This document records the governance decision for the breakout-related daily
stock model review.

It does not change production model conditions, scoring, ranking, PDF layout,
research baselines, or model contracts.

## Collaboration Boundary

The model-governance agent owns execution coordination. That includes technical
implementation, validator selection, branch/PR flow, cross-lane task routing,
opening or assigning Codex conversations, and progress reporting.

The user owns model-direction decisions. Those decisions include whether a model
should exist, whether a condition matches the intended trading logic, and
whether the current model-change direction is acceptable.

The agent must convert code-level or implementation-level review needs into
business logic, model-boundary, or condition questions before asking the user.
The user is not expected to perform code review.

## Current Decision

Taiwan stock taxonomy should be owned by a dedicated conversation role inside
the Taiwan stock recommendation project family.

Recommended role id:

```text
tw_stock_taxonomy_maintenance
```

This role belongs under the existing Taiwan stock recommendation project. It is
not a separate visible Codex project by default. It should own market taxonomy
surfaces such as:

- mainstream versus non-mainstream grouping;
- theme and industry mapping;
- hot-theme classification;
- theme-level fund rotation inputs used by `group_fund_rotation`;
- taxonomy contracts or validation rules that feed daily model and PDF
  consumers.

The taxonomy role must not directly change production stock-entry model scoring
or ranking. It provides classification inputs that formal model contracts may
consume.

## Research Data Governance

Backtest input data and result registries should be owned by the
`research_backtest` lane, not by production model maintenance.

The research/backtest lane should own:

- historical price data versions;
- TDCC historical data versions;
- revenue history versions;
- feature snapshots used for backtests;
- backtest result registries;
- evidence required before promotion.

Production model maintenance may read research results for parity and
promotion decisions, but it must not write research variants into the
production baseline without an explicit promotion or synchronization PR.

## Three-Layer Model Structure

The breakout model review should use three layers.

### 1. Taxonomy Layer

This layer classifies market context and stock themes. It does not select
stocks by itself.

Examples:

- mainstream / non-mainstream;
- hot theme;
- theme fund rotation;
- industry or concept grouping.

Owner: `tw_stock_taxonomy_maintenance` once registered.

### 2. Breakout Event Feature Layer

This layer should calculate reusable breakout facts, but it should not become a
shared hard gate that silently changes multiple models.

Useful breakout event features include:

- volume expansion flag and magnitude;
- breakout reference type;
- breakout reference price;
- breakout magnitude percentage;
- close position within the signal day;
- price position within a recent range such as 120 trading days;
- over-extension flag;
- failed-breakout or false-breakout risk flags.

The reference type must stay explicit. A previous-N-day high, range high,
platform high, and neckline are not interchangeable.

Recommended reference-type examples:

```text
previous_n_day_high
range_high
platform_high
w_bottom_neckline
structured_neckline
```

This layer may be introduced only with explicit consumer boundaries and
validators. It should not rewrite existing `volume_range_breakout` behavior in
the first implementation.

### 3. Stock Entry Model Layer

This layer decides whether a stock enters a formal stock-entry model and how it
is scored or ranked.

The current review group is:

| model_id | Recommended role in the group |
|---|---|
| `volume_range_breakout` | Keep as the current production baseline for bottom/base volume attack. Do not rewrite it as a shared pre-filter in the first change. It is the only current stock model with research parity status `ok`. |
| `w_bottom_right_side` | Review as a low-position W-bottom structure model. If converted to confirmation behavior, its neckline breakout and volume confirmation must be explicit. |
| `neckline_volume_breakout_confirmation` | Current formal v1 model for W-bottom neckline volume breakout confirmation. It is not the generic neckline family, and it does not include inverse head-and-shoulders, triple bottom, or structured-bottom-other subtypes. |

### `volume_range_breakout` Meaning

`volume_range_breakout` is not defined by "previous high" semantics and is not a
model targeted for removal in this review.

The intended business meaning is:

```text
Bottom/base volume attack after a contracted consolidation base.
```

In this context, "range" means a controlled, volume-contracted consolidation
base near a lower or recovering price position. It does not mean a broad
high-low trading range, a high-position box breakout, or any arbitrary
high breakout.

The current production implementation needs a computable breakout line, so it
uses the highest price in the recent 20 trading sessions as a short local base
ceiling. Twenty sessions is intentionally short and should be understood as a
trigger threshold for a recent contracted base, not as the model's business
meaning. If future evidence shows that the trigger admits too many
high-position or wide-range breakouts, the fix should be a formal
`volume_range_breakout` model-change PR that tightens low-position, base-width,
volume-contraction, and candle-quality rules. It should not be silently
replaced by `neckline_volume_breakout_confirmation`.

## Breakout Gate Decision

A common "volume breakout first, then classify into models" idea is useful as
an analysis frame, but it should not be implemented as a shared hard gate yet.

Reason:

- `volume_range_breakout` is intended to capture bottom/base volume attack from
  a controlled consolidation base. Its current recent-20-session local base
  ceiling is only the breakout threshold; it must not become the model
  definition.
- `w_bottom_right_side` depends on a W-bottom neckline and low-position
  structure, but remains the early-entry/right-side model before neckline
  confirmation.
- `neckline_volume_breakout_confirmation` v1 represents only W-bottom neckline
  volume breakout confirmation. Other neckline families require separate
  research, contract updates, and promotion evidence before production use.

If all three models first pass through one fixed N-day-high breakout gate, the
models will look different by name while actually sharing the same selection
logic. That would weaken model ownership and make later review harder.

The safer path is to compute breakout event features first, then let each model
choose its own reference type and position rules.

## Neckline Definition Rule

Do not label a model as a neckline model if it only uses generic previous-high
or 60-day-high distance fields.

The current code has two different behaviors:

- `near_high_neckline_challenge` reads already-computed pressure-distance
  fields and may fall back to previous high or 60-day high semantics.
- `w_bottom_right_side` can infer a W-bottom neckline from price history.

For any new neckline confirmation model, the implementation spec must state:

- how the neckline price is found;
- which price history window is used;
- whether the reference is a W-bottom neckline, another structured neckline, or
  a generic pressure high;
- how `close / neckline - 1` is signed;
- what range counts as confirmed breakout;
- what range counts as over-extended.

The existing W-bottom detector defines a W-bottom neckline as the highest high
between two qualifying troughs. It uses recent price history, requires the two
troughs to be close in height, rejects stale right troughs, and calculates:

```text
neckline_distance_pct = (current_close / neckline - 1) * 100
```

For this convention:

- negative means the close is below the neckline;
- zero means the close is at the neckline;
- positive means the close is above the neckline.

## Position-Level Rule

The user intent for the current review is:

- `volume_range_breakout` and `w_bottom_right_side` should generally be
  low-position or base breakout models.
- `neckline_volume_breakout_confirmation` v1 is the W-bottom confirmed-breakout
  counterpart to `w_bottom_right_side`. It may occur after the base has moved
  away from the right low, but it should not be reinterpreted as every possible
  neckline breakout pattern.

The implementation should calculate an explicit position metric before tuning
thresholds. A likely feature is:

```text
price_position_120d = (close - low_120d) / (high_120d - low_120d)
```

Thresholds such as low, mid, and high position must be validated in
research/backtest before being promoted to production.

## TDCC And Revenue Role

For the first formal design, TDCC and revenue should not become entry hard
gates unless research evidence explicitly supports that promotion.

Recommended initial role:

- TDCC positive behavior can be a score bonus.
- TDCC distribution or weakening can be a score penalty or risk tag.
- Revenue growth or catalyst evidence can be a score bonus.
- Revenue deterioration can be a score penalty or risk tag.

The model contract must document whether each input is an entry condition,
score component, penalty, or display-only risk label.

## One-Year Data Limitation

The current approximate one-year history is enough for:

- sanity checks;
- visual review against human-recognizable patterns;
- selection count checks;
- model-overlap checks;
- D+5 / D+10 / D+20 exploratory outcome checks;
- threshold sensitivity review.

It is not enough for:

- full-cycle bull, bear, and range-market proof;
- final long-term alpha claims;
- stable threshold optimization;
- strong TDCC or revenue causality claims.

## Formal Implementation Path

1. Register or document `tw_stock_taxonomy_maintenance` in the project-level
   conversation lane registry before taxonomy implementation starts.
2. Let `research_backtest` own backtest data governance and feature/result
   evidence registries.
3. Keep `volume_range_breakout` unchanged as the current production baseline
   during the first neckline model design.
4. Produce a formal `neckline_volume_breakout_confirmation` model-change spec
   before editing production code. The current spec is
   `docs/specs/neckline_volume_breakout_confirmation_model_change_spec.md`.
   The implemented v1 is scoped to W-bottom neckline volume breakout
   confirmation only.
5. Implement production model changes only in `daily_model_maintenance`.
6. Update `config/stock_model_contract_registry.csv` and
   `config/model_surface_registry.csv` only when the formal production surface
   is implemented.
7. Run stock contract, daily PDF consumer, research parity, and model surface
   validators before PR review.

## Forbidden Shortcuts

- Do not reactivate `near_high_neckline_challenge` or `platform_strengthening`
  without a formal model-change PR.
- Do not broaden `neckline_volume_breakout_confirmation` beyond the W-bottom
  subtype without production code, tests, parity handling, and contract updates.
- Do not rewrite `volume_range_breakout` into a shared pre-filter as the first
  step.
- Do not copy research variants into the production baseline.
- Do not modify PDF-side scoring or ranking.
- Do not add in-repo code that self-triggers GitHub Actions.

## Required Validators For The Formal Model-Change PR

When a formal model-change PR is eventually opened, run at minimum:

```text
python scripts/validate_model_surface_registry.py
python scripts/validate_stock_model_contract_registry.py
python scripts/validate_daily_pdf_contract_consumers.py
python scripts/validate_research_against_stock_model_contract.py
python scripts/validate_daily_model_research_parity.py
python scripts/validate_repo_semantic_integrity.py
```
