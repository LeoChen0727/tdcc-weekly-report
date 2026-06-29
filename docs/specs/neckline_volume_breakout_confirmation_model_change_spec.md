# Neckline Volume Breakout Confirmation Model Change Spec

This document defines the production model-change contract for
`neckline_volume_breakout_confirmation`.

Implementation status as of the 2026-06-29 production sync:

- `neckline_volume_breakout_confirmation` is promoted through
  `neckline_strict_45_signal_90_score_v1`.
- The formal condition requires 45-session non-bearish pre-signal context.
- The 90-session context is score/risk adjustment only, not an entry exclusion.
- The formal operation evidence is stored in
  `output/latest/approved_operation_patterns_latest.csv`.
- Raw research candidate rows remain advisory-only unless a later PR promotes a
  new approval version.

Earlier sections in this document still explain the review logic and rollout
boundary that led to the production sync. Future changes should add a new
approval version instead of mutating the meaning of this v1 silently.

## Purpose

The intended model is a confirmed neckline breakout with volume expansion. It
is not a generic previous-high breakout, not a near-pressure watch signal, and
not a platform-inside strengthening signal.

The broader breakout review should be split into two model families:

| model family | proposed model_id | meaning |
|---|---|---|
| descending resistance breakout | `descending_resistance_volume_breakout` | Price breaks above a descending resistance line drawn from audited swing highs. This is not a neckline model. |
| bottom-pattern neckline breakout | `neckline_volume_breakout_confirmation` | Price breaks above the neckline of an audited bottoming pattern such as W-bottom, inverse head-and-shoulders, triple bottom, or another structured bottom. |

This PR documents the neckline family. The descending-resistance family should
be specified and implemented separately so swing-high resistance lines are not
misclassified as necklines.

The model should eventually replace or reduce the need for these currently
blocked or overlapping production surfaces:

- `near_high_neckline_challenge`
- `platform_strengthening`

Those existing model ids must not be deleted or deprecated until a formal
production model-change PR updates code, contracts, tests, and parity handling.

## Current Production Evidence

Current production behavior shows three different concepts:

| model_id | current production meaning | issue for this change |
|---|---|---|
| `volume_range_breakout` | bottom/base volume attack after controlled consolidation; current code uses the recent-20-session local base ceiling as the trigger threshold | Keep unchanged as current baseline. It is the only current stock model with research parity status `ok`, and it is not a target for removal in this neckline review. |
| `w_bottom_right_side` | W-bottom right-side setup near the neckline, before confirmed breakout | Useful structured neckline source, but current entry condition rejects already-confirmed breakouts. |
| `near_high_neckline_challenge` | near pressure before confirmed breakout | Condition and scoring use opposite sides of the distance sign convention. |
| `platform_strengthening` | platform-inside strengthening before confirmed breakout | Not a confirmed breakout model. |

`volume_range_breakout` must be described from the base structure and volume
attack, not from the field name used to compute the breakout threshold. Its
intended business meaning is bottom/base volume attack: price leaves a
controlled, volume-contracted consolidation base with clear volume expansion or
a locked-limit-up exception. In this model, "range" means the consolidation
base, not a broad high-low range and not a high-position box breakout.

The current production trigger still needs a computable breakout standard, so
it uses the highest price in the recent 20 trading sessions as a short local
base ceiling. Twenty sessions is intentionally short and should be understood
as the breakout line for a recent contracted base, not as the business
definition. If future review finds the production condition too loose, the
correct action is to tighten `volume_range_breakout` through its own
model-change PR, especially around low-position, base-width,
volume-contraction, and candle-quality rules. It should not be folded into or
replaced by `neckline_volume_breakout_confirmation`.

The confirmed blocker for `near_high_neckline_challenge` is:

- production condition accepts pressure distance `0..5`, meaning price is at or
  above the pressure level by up to 5%;
- scoring rewards pressure distance `-5..0`, meaning price is below the
  pressure level by up to 5%;
- research proxy follows the below-pressure scoring side more closely than the
  production condition.

Therefore the next production change should not tune the old model in place.
It should create an explicit confirmed-breakout model and then decide whether
the old pre-breakout surfaces should remain, be downgraded, or be deprecated.

`w_bottom_right_side` is different. It should remain a pre-breakout observation
surface for W-bottom right-side or second-bottom formation. It should not be
deleted or folded into the confirmed-breakout model as the first step.

## Proposed Model Identity

```text
model_id: neckline_volume_breakout_confirmation
model_name: Neckline volume breakout confirmation
owner_lane: daily_model_maintenance
selection_level: individual_stock
surface_type: stock_entry_model
```

Business meaning:

```text
The stock has closed above an auditable neckline reference with clear volume
confirmation. Signal-day candle quality affects score and risk tags, not
whether the neckline breakout exists.
```

## Neckline Reference Rule

Do not call the signal a neckline model if the implementation only uses a
generic previous-N-day high or 60-day high.

The neckline model should expose a `neckline_pattern_subtype` field. Initial
subtypes:

| subtype | meaning | first implementation status |
|---|---|---|
| `w_bottom` | two qualifying troughs with the neckline at the rebound high between them | first implementation priority because current production code already has W-bottom geometry support |
| `inverse_head_and_shoulders` | left shoulder, lower head, right shoulder, with neckline through the two rebound highs | backlog until a dedicated detector exists |
| `triple_bottom` | three bottom attempts under a shared resistance or neckline zone | backlog until a dedicated detector exists |
| `structured_bottom_other` | bottoming structure with an auditable neckline but not confidently classified into the above subtypes | allowed only with strict audit fields; must not become a generic previous-high breakout bucket |

Allowed neckline references, in priority order:

1. `w_bottom_neckline`: the highest high between two qualifying troughs from
   the existing W-bottom price-history detector.
2. `structured_neckline`: a future audited structured-neckline detector with a
   documented window, reference price, and distance field.
3. `explicit_upstream_neckline_breakout`: an upstream row that explicitly marks
   `neckline_breakout_flag=true` or
   `volume_breakout_type=neckline_volume_breakout` and provides an audited
   neckline distance field.

Rejected references:

- `previous_20d_high` by itself;
- `previous_60d_high` by itself;
- `range_high` by itself;
- `platform_high` by itself;
- broad `pattern` text without a price-history or audited upstream neckline
  reference.

If only a generic high or range-high reference exists, the stock may belong to
`volume_range_breakout` only when it also fits the bottom/base volume attack
intent. A generic high or wide-range breakout must not enter
`neckline_volume_breakout_confirmation`, and should not be treated as a clean
`volume_range_breakout` candidate without the bottom/base context.

## W-Bottom Two-Stage Treatment

W-bottom should be treated as two separate surfaces:

| stage | model_id | meaning |
|---|---|---|
| pre-breakout / right-side formation | `w_bottom_right_side` | The second bottom or right side is forming near the lower structure, before confirmed neckline breakout. |
| confirmed neckline breakout | `neckline_volume_breakout_confirmation` with `neckline_pattern_subtype=w_bottom` | The stock has broken above the W-bottom neckline with volume confirmation or locked-limit-up confirmation, and the second W arc has stronger average participation than the first arc baseline. |

The first stage is important because the user wants W-bottom candidates before
the neckline has broken. The second stage is the confirmed breakout model.
Both stages must audit second-arc participation quality.

For `w_bottom_right_side`, shape alone is not enough. The production
implementation should audit and prioritize second-bottom volume quality:

```text
second_arc_volume_ratio =
  second_arc_avg_volume / first_arc_avg_volume
```

For `neckline_volume_breakout_confirmation` with
`neckline_pattern_subtype=w_bottom`, this is not only a score bonus. The
confirmed W-bottom neckline breakout must also pass the W-bottom second-arc
participation rule:

```text
w_bottom_second_arc_volume_quality_ok =
  second_arc_avg_daily_volume > first_arc_month_avg_volume
```

This W-bottom arc-volume rule is separate from signal-day volume confirmation.
Locked or near-locked limit-up may bypass the normal signal-day `volume_ratio`
and `volume_ma20_lots` gates, but it must not bypass the W-bottom arc-volume
quality audit.

For W-bottom arc-volume calculation, include all trading days in the selected
first-arc and second-arc windows. Do not exclude limit-up days from the arc
average and do not add a separate limit-up distortion flag for this model. The
limit-up exception applies only to the signal-day volume gate, not to the
first-arc / second-arc average-volume comparison.

Recommended interpretation:

| second_arc_volume_ratio | treatment |
|---|---|
| `< 1.0` | weak second bottom; reject or risk-tag because the second formation has less participation than the first |
| `1.0..1.2` | only weak confirmation; do not rank as high-confidence W-bottom |
| `>= 1.2` | minimum expected volume-quality confirmation for second-bottom formation |
| `>= 1.5` | strong second-bottom participation; add score |

The exact production field names must be audited before code changes. Current
production code already has a related `volume_ratio_2_vs_1` concept, but the
implementation PR must verify whether that field compares the intended second
arc daily average volume against the intended first arc monthly average volume.
Do not silently treat a single signal-day volume spike, a generic `volume_ratio`,
or the current field name as proof that this requirement has been met.

Recommended window definition for the implementation PR:

| window | definition |
|---|---|
| first arc monthly baseline | month-like average volume around the first trough / first rebound arc, using all trading days in the audited production window chosen in the implementation PR |
| second arc daily average | bars from the second trough through the current right-side formation, using average daily volume across all trading days in the window instead of only the latest day |

If the right-side formation is too new and does not have enough bars for a
stable second-arc average, it may remain a lower-confidence watch candidate but
must not be promoted as a high-confidence W-bottom signal.

## Sign Convention

Use this convention for all neckline distance fields:

```text
neckline_distance_pct = (close / neckline_price - 1) * 100
```

Interpretation:

| range | meaning |
|---|---|
| `< 0` | close is below the neckline |
| `0` | close is at the neckline |
| `> 0` | close is above the neckline |

The confirmed breakout floor for the first implementation should be:

```text
neckline_distance_pct >= 0
```

Initial distance handling:

| neckline_distance_pct | treatment |
|---|---|
| `< 0` | reject; this is still a challenge/watch setup, not confirmed breakout |
| `0..3` | strongest confirmation score zone |
| `3..5` | acceptable confirmation score zone |
| `> 5` | still eligible if the neckline reference is audited; do not reject or penalize solely because the breakout distance is large |

Do not add a generic "price extension is too high" exclusion or penalty in the
first implementation. Breakout quality should be handled through candle-quality
score components, false-breakout risk tags, TDCC/revenue inputs, and later
research evidence.

## Initial Entry Condition Proposal

The production implementation should create a new independent condition
function. It must not rewrite `cond_volume_breakout`,
`cond_w_bottom_right`, `cond_neckline_challenge`, or
`cond_platform_strength` as shared hard gates.

Recommended condition:

```text
has_audited_neckline_reference
and neckline_distance_pct >= 0
and w_bottom_second_arc_volume_quality_ok when neckline_pattern_subtype == w_bottom
and has_volume_confirmation
```

Where:

```text
has_audited_neckline_reference =
  detected W-bottom neckline context is available
  or audited structured-neckline context is available
  or explicit upstream neckline breakout flag/type is present with audited
     distance fields
```

Recommended first implementation for `has_volume_confirmation`:

```text
locked_limit_up_neckline_breakout
or (
  volume_ratio >= 2.0
  and volume_ma20_lots >= 1000 when volume_ma20_lots is available
)
```

Locked-limit-up handling must bypass the normal `volume_ratio` and
`volume_ma20_lots` gates. This follows the existing `volume_range_breakout`
rule that locked or near-locked limit-up breakouts do not require volume ratio
or 20-day average volume confirmation.

```text
locked_limit_up_neckline_breakout =
  neckline_distance_pct >= 0
  and daily_return_pct >= 9.0
  and close >= high * 0.995
  and open >= close * 0.995
  and (high == low or intraday_range_pct_vs_prev_close <= 1.0)
```

If the implementation cannot prove the signal day is a true locked or
near-locked limit-up day using price fields, it must use the normal volume
confirmation path.

## Position-Level Rule

This model is intended to represent a mid-to-high-position neckline
confirmation. It should not require the same low-position rule as
`volume_range_breakout` or `w_bottom_right_side`.

Recommended feature:

```text
price_position_120d = (close - low_120d) / (high_120d - low_120d)
```

Initial interpretation:

| price_position_120d | treatment |
|---|---|
| `< 0.35` | low-position; likely belongs to W-bottom or range breakout review |
| `0.35..0.80` | preferred mid-position confirmation zone |
| `> 0.80` | high-position; eligible, but should be labeled for review rather than automatically rejected or penalized |

Do not block the first implementation solely because `price_position_120d` is
unavailable. If it is unavailable, register the input as pending for research
validation. Do not use missing or high `price_position_120d` as a hidden
rejection rule.

## Initial Scoring Proposal

The new score profile must be independent. Do not reuse an existing profile in
a way that makes future tuning of another model change this model.

Recommended score components:

| component | proposed role |
|---|---|
| base score | base confirmation score for passing the entry condition |
| neckline reference quality | bonus for W-bottom or audited structured neckline; smaller bonus for explicit upstream-only neckline |
| distance quality | strongest bonus for `0..3`, smaller bonus for `3..5`; no automatic penalty above 5 |
| volume strength | bonus above `2.0`, capped; extra bonus above `3.0` on non-limit-up signals |
| W-bottom second-arc volume quality | required for `neckline_pattern_subtype=w_bottom`; add score when the second arc average volume is materially above the first arc monthly baseline |
| locked-limit-up breakout | bonus and normal volume-gate bypass when the signal day is locked or near-locked limit-up |
| candle body quality | bonus for strong red body; penalty if the red body is too short for a confirmed breakout attack |
| close quality | bonus when close is near the signal-day high |
| upper-shadow quality | penalty for long upper shadow on the signal day |
| repeated upper-shadow behavior | penalty or risk tag when recent candles repeatedly show long upper shadows after attack attempts |
| TDCC positive behavior | score bonus only, not entry hard gate |
| TDCC distribution or weakening | penalty or risk tag |
| revenue growth or catalyst evidence | score bonus only, not entry hard gate |
| revenue deterioration | penalty or risk tag |
| false-breakout risk | penalty or risk tag |

TDCC and revenue must not become entry hard gates in the first implementation
unless research evidence explicitly supports that promotion.

Recommended candle-quality scoring should reference the existing
false-breakout and volume-attack quality rules:

| candle feature | proposed scoring treatment |
|---|---|
| strict red candle quality | add score when red candle, real body >= 40% of intraday range, upper shadow <= 25% of intraday range, and close location >= 75% |
| relaxed red candle quality | smaller add score when red candle, real body >= 25%, upper shadow <= 35%, and close location >= 65% |
| short red body | subtract score or add risk tag when the candle is red but real body is below 25% of intraday range |
| failed close / not red | subtract score or add risk tag unless the day is a locked or near-locked limit-up breakout |
| long upper shadow | subtract score using a capped penalty; production may reuse the existing `upper_shadow_pct_of_close > 3.0` penalty pattern or the research `upper_shadow_pct_of_range > 35` quality rule |
| repeated upper shadows | subtract score or add risk tag when recent attack candles repeatedly meet the long-upper-shadow definition |

The production PR must choose exact field names for these candle inputs and
register them in `config/stock_model_contract_registry.csv`.

## Contract Requirements

The production implementation owns these files together:

```text
config/daily_model_condition_spec.csv
config/stock_model_contract_registry.csv
config/model_surface_registry.csv
tests/test_daily_candidate_model_layer.py
tests/test_stock_model_contract_registry.py
tests/test_model_surface_registry.py
```

The contract must state:

- exact `condition_function`;
- exact `score_function`;
- exact `score_profile_id`;
- input columns used for entry condition;
- input columns used only for score bonus;
- input columns used only for penalties or risk tags;
- `approved_for_daily_pdf`;
- `approved_for_tdcc_weekly_pdf`;
- `approved_for_individual_pdf`;
- research parity status.

Do not change `neckline_volume_breakout_confirmation` in formal registries
without matching production code, tests, and research/parity handling in the
same PR.

## Deprecation Plan For Existing Surfaces

Do not delete old model ids as the first implementation step.

Recommended rollout:

1. Add `neckline_volume_breakout_confirmation` as a new independent model.
2. Validate selection counts and overlap against
   `near_high_neckline_challenge`, `platform_strengthening`,
   `w_bottom_right_side`, and `volume_range_breakout`.
3. If the new model covers the intended confirmed-breakout surface, mark
   `near_high_neckline_challenge` and/or `platform_strengthening` as deprecated
   through contract fields in a separate explicit model-change step.
4. Only remove old code after contracts, tests, daily PDF consumers, and
   research/backtest parity no longer require those model ids.

## Research And Parity Requirements

Research/backtest remains advisory-only.

Expected first parity state after production implementation may be one of:

- `missing_research_baseline`, if no matching research model exists yet;
- `warning_research_variant_only`, if research has a proxy or variant;
- `ok`, only if research/backtest confirms the production condition and scoring
  contract exactly enough for parity.

Do not write research recommendations, research variants, or backtest-optimized
thresholds directly into the production baseline.

If research/backtest is not aligned after the production PR, report that the
`research_backtest` lane needs synchronization or open a separate promotion/sync
PR only when explicitly requested.

## Required Validation For Production PR

When production code is changed, run at minimum:

```text
python scripts/validate_model_surface_registry.py
python scripts/validate_stock_model_contract_registry.py
python scripts/validate_daily_pdf_contract_consumers.py
python scripts/validate_research_against_stock_model_contract.py
python scripts/validate_daily_model_research_parity.py
python scripts/validate_repo_semantic_integrity.py
python -m pytest tests/test_daily_candidate_model_layer.py tests/test_stock_model_contract_registry.py tests/test_model_surface_registry.py -q
```

This spec-only change should run repository governance validators, but it does
not require production model parity to change because no production model
condition, scoring, ranking, or contract row is edited here.
