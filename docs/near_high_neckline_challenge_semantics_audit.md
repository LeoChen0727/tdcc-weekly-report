# Near High Neckline Challenge Semantics Audit

This audit records the distance-field semantics for
`near_high_neckline_challenge`.

It does not change production model conditions, scoring, ranking, research
baselines, or PDF behavior.

## Audit Result

`near_high_neckline_challenge` has a confirmed sign-semantics blocker.

The shared distance convention is:

- negative value: current close is below the referenced pressure level;
- zero: current close is at the referenced pressure level;
- positive value: current close is above the referenced pressure level.

The current production condition and scoring do not use that convention in the
same direction.

## Evidence

The production condition uses the distance helpers in this order:

```text
neckline_distance_pct
distance_to_previous_high_pct
distance_to_previous_60d_high_pct
```

The condition currently accepts distances from `0` to `5`. That means the
condition favors stocks at or above the referenced pressure level by up to 5%.

The production score uses the distance helpers in this order:

```text
distance_to_neckline_pct
distance_to_prior_high_pct
distance_to_previous_60d_high_pct
```

The score bonus currently rewards distances from `-5` to `0`. That means scoring
favors stocks still below the referenced pressure level, especially from 0% to
2% below.

The research proxy also uses the below-pressure convention. It describes the
baseline as within 5% below the 60-day high and uses a range of `-5` to `0`.

## Conclusion

The current surface is not ready for parameter tuning.

Before any production tuning, this model needs a formal decision on intended
business meaning:

- Option A: "near pressure from below" means `-5 <= distance <= 0`.
- Option B: "just reclaimed / slightly above pressure" means `0 <= distance <= 5`.
- Option C: split the surface into two explicitly named behaviors.

Changing the production condition from one side of the pressure level to the
other would change selected stocks, so it must be treated as a formal production
model change.

## Required Follow-up

Owner: `daily_model_maintenance`

Next action:

1. Decide the intended business meaning using a formal model-change PR.
2. Update production condition and scoring together if a change is approved.
3. Update `config/stock_model_contract_registry.csv` only if the contract
   surface changes.
4. Re-check research/backtest parity.

Do not copy the research proxy into production as a shortcut. The research proxy
is advisory until an explicit promotion or synchronization PR is approved.
