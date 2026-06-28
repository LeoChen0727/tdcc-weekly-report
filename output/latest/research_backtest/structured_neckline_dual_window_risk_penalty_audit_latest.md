# Structured-Neckline Dual Window Risk Penalty Audit

- research_id: `structured_neckline_dual_window_risk_penalty_audit`
- parameter_set_id: `structured_neckline_dual_window_risk_penalty_audit_20260629`
- source_rule_id: `dual_45_entry_90_risk_warning`
- risk_penalty_scope_id: `dual_window_45_pass_90_bearish_risk_penalty_grid`
- source_events: `374`
- detail_rows: `6358`
- approved_for_daily: `false`
- production_readiness: `not_production_ready_research_only`

## Low-Position Bull Accepted Overall

- broad_45_non_bearish_with_90_warning: sample=`87`, success=`70.1149`, pure_win=`60.6061`, avg_return_pct=`3.8213`, median_return_pct=`3.8202`
- confirmed_plus_risk_drawdown90_ge_neg20: sample=`48`, success=`79.1667`, pure_win=`72.9730`, avg_return_pct=`5.5353`, median_return_pct=`10.3780`
- confirmed_plus_risk_drawdown90_ge_neg25: sample=`53`, success=`77.3585`, pure_win=`69.2308`, avg_return_pct=`5.0924`, median_return_pct=`10.1493`
- confirmed_plus_risk_mild_damage_return90_ge_neg10_drawdown90_ge_neg25: sample=`51`, success=`76.4706`, pure_win=`69.2308`, avg_return_pct=`5.1551`, median_return_pct=`10.2009`
- confirmed_plus_risk_penalty_le_1: sample=`49`, success=`77.5510`, pure_win=`71.0526`, avg_return_pct=`5.3373`, median_return_pct=`10.3571`
- confirmed_plus_risk_penalty_le_2: sample=`51`, success=`76.4706`, pure_win=`69.2308`, avg_return_pct=`5.2544`, median_return_pct=`10.2009`
- confirmed_plus_risk_penalty_le_3: sample=`53`, success=`75.4717`, pure_win=`68.2927`, avg_return_pct=`4.9734`, median_return_pct=`10.1911`
- confirmed_plus_risk_return90_ge_neg10: sample=`58`, success=`72.4138`, pure_win=`64.4444`, avg_return_pct=`4.1742`, median_return_pct=`7.4889`
- confirmed_plus_risk_return90_ge_neg5: sample=`50`, success=`80.0000`, pure_win=`73.6842`, avg_return_pct=`5.8316`, median_return_pct=`10.3780`
- confirmed_plus_risk_short_return45_ge_5: sample=`65`, success=`72.3077`, pure_win=`64.0000`, avg_return_pct=`4.1368`, median_return_pct=`4.8414`
- confirmed_plus_risk_short_return45_ge_8: sample=`58`, success=`77.5862`, pure_win=`70.4545`, avg_return_pct=`5.0508`, median_return_pct=`10.1960`
- confirmed_plus_risk_short_slope45_ge_2: sample=`61`, success=`75.4098`, pure_win=`68.0851`, avg_return_pct=`4.9162`, median_return_pct=`10.1493`
- confirmed_plus_risk_short_strength_return45_ge_5_slope45_ge_2: sample=`58`, success=`75.8621`, pure_win=`68.8889`, avg_return_pct=`5.0351`, median_return_pct=`10.1960`
- confirmed_plus_risk_slope90_ge_0: sample=`50`, success=`76.0000`, pure_win=`69.2308`, avg_return_pct=`5.3067`, median_return_pct=`10.2790`
- confirmed_plus_risk_slope90_ge_neg2: sample=`51`, success=`76.4706`, pure_win=`69.2308`, avg_return_pct=`5.2738`, median_return_pct=`10.2009`
- confirmed_plus_risk_strict_repair_return45_ge_5_slope45_ge_2_return90_ge_neg15: sample=`52`, success=`76.9231`, pure_win=`70.0000`, avg_return_pct=`5.1913`, median_return_pct=`10.2790`
- strict_45_90_non_bearish: sample=`48`, success=`79.1667`, pure_win=`72.9730`, avg_return_pct=`5.5353`, median_return_pct=`10.3780`

## Manual Alignment

- broad_45_non_bearish_with_90_warning: good_rejected=`1/9`, bad_accepted=`0/1`
- confirmed_plus_risk_drawdown90_ge_neg20: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_drawdown90_ge_neg25: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_mild_damage_return90_ge_neg10_drawdown90_ge_neg25: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_penalty_le_1: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_penalty_le_2: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_penalty_le_3: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_return90_ge_neg10: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_return90_ge_neg5: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_short_return45_ge_5: good_rejected=`1/9`, bad_accepted=`0/1`
- confirmed_plus_risk_short_return45_ge_8: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_short_slope45_ge_2: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_short_strength_return45_ge_5_slope45_ge_2: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_slope90_ge_0: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_slope90_ge_neg2: good_rejected=`2/9`, bad_accepted=`0/1`
- confirmed_plus_risk_strict_repair_return45_ge_5_slope45_ge_2_return90_ge_neg15: good_rejected=`2/9`, bad_accepted=`0/1`
- strict_45_90_non_bearish: good_rejected=`2/9`, bad_accepted=`0/1`

## Boundary

- This is a research-only risk penalty grid for the 45-session pass / 90-session bearish-risk group.
- It is not a production score, rank, filter, or model condition.
- It does not write research variants back to production baseline.
