# W Bottom Research Overlap Guardrail Contract

This contract applies to research-only `w_bottom_right_side` backtest grids,
parameter matrices, stop-loss audits, and market-regime review artifacts.

## Rule

W-bottom research grids may intentionally expand the same source event across
entry rules, exit rules, horizons, filters, or market-regime slices. Those
expanded event-level rows are diagnostic surfaces only.

When a strategy group still contains multiple same-stock events whose holding
windows overlap, that group must not be cited as promotion evidence until a
same-stock non-overlap basis is published.

For this contract, same-stock active-window overlap means:

- same `stock_id`;
- later row's `entry_date` is on or before an earlier accepted row's
  `exit_date`;
- rows are compared only inside the same strategy key, such as `surface_id`,
  `event_set_id`, `entry_rule_id`, `outcome_rule_id`, `condition_set_id`,
  `parameter_set_id`, and `signal_market_regime` when those columns exist.

## Guardrail Artifact

The current guardrail is:

- `output/latest/research_backtest/w_bottom_research_overlap_guardrails_latest.csv`
- `output/latest/research_backtest/w_bottom_research_overlap_guardrails_latest.md`
- `output/history/research/w_bottom_research_overlap_guardrails.csv`

Rows with `overlap_pair_count > 0` must carry:

```text
promotion_evidence_status=blocked_requires_same_stock_non_overlap_artifact
required_followup=publish_same_stock_non_overlap_basis_before_promotion_evidence
```

Rows may remain in the research grid for diagnostics, but they remain
`approved_for_daily=False` and
`production_readiness=not_production_ready_research_only`.

## Validator

Run:

```text
python scripts/validate_w_bottom_research_overlap_guardrails.py
```

The validator fails closed when overlapping W-bottom strategy rows are not
blocked from promotion evidence, source artifacts are marked production-ready,
latest/history guardrails diverge, or the markdown summary omits the
same-stock non-overlap requirement.
