# Calendar Data Source Status

- generated_at: `2026-09-05 18:13:06 Asia/Taipei`
- policy: Official/known-calendar sources are stored. Missing or blocked sources remain pending instead of being fabricated.

| source | status | rows | url | note |
|---|---|---:|---|---|
| twse_ex_right_ex_dividend | ok | 82 | https://www.twse.com.tw/rwd/zh/exRight/TWT48U?response=json |  |
| twse_shareholder_meeting_from_dividend_distribution | ok | 549 | https://openapi.twse.com.tw/v1/opendata/t187ap45_L | TWSE-listed shareholder meeting dates parsed from official OpenAPI t187ap45_L when available. |
| monthly_revenue_expected_window | rule_based_expected_window | 365 | https://mops.twse.com.tw/mops/web/t05st10_ifrs | Expected monthly revenue publication window generated for tracked stocks; not a confirmed company catalyst. |
| federal_reserve_fomc | ok | 11 | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm |  |
| bea_release_schedule | ok | 13 | https://www.bea.gov/news/schedule |  |
| bls_cpi_release_schedule | ok | 4 | https://www.bls.gov/schedule/news_release/cpi.htm | Parsed 4 release rows from the official BLS schedule table. |
| bls_employment_release_schedule | ok | 4 | https://www.bls.gov/schedule/news_release/empsit.htm | Parsed 4 release rows from the official BLS schedule table. |
| mops_shareholder_meeting_calendar | partial_coverage_twse_only | 549 | https://mops.twse.com.tw/mops/web/t108sb31new | TWSE-listed shareholder meeting dates are stored from t187ap45_L. Direct MOPS shareholder pages are blocked or unavailable from this environment, and OTC coverage still needs a stable official endpoint. |

## What Is Already Stored

- TWSE ex-right/ex-dividend calendar is stored when the official endpoint returns rows.
- Monthly revenue expected windows are generated from Taiwan reporting rules for tracked stocks.
- FOMC and BEA macro dates are stored when official pages are reachable.

## Pending Sources

- TWSE shareholder meeting dates are stored from official OpenAPI where available; MOPS/TPEX coverage remains pending if blocked.
- BLS CPI/employment schedules are stored when official schedule tables are reachable and parseable.
- Company-specific technology validation, exhibitions, law conferences, and news catalysts need explicit source rows in event_catalyst_log.csv before they can affect stock ranking.
