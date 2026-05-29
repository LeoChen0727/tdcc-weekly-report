# Calendar Data Source Status

- generated_at: `2026-05-29 18:05:44 Asia/Taipei`
- policy: Official/known-calendar sources are stored. Missing or blocked sources remain pending instead of being fabricated.

| source | status | rows | url | note |
|---|---|---:|---|---|
| twse_ex_right_ex_dividend | ok | 120 | https://www.twse.com.tw/rwd/zh/exRight/TWT48U?response=json |  |
| monthly_revenue_expected_window | rule_based_expected_window | 479 | https://mops.twse.com.tw/mops/web/t05st10_ifrs | Expected monthly revenue publication window generated for tracked stocks; not a confirmed company catalyst. |
| federal_reserve_fomc | ok | 13 | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm |  |
| bea_release_schedule | failed | 0 | https://www.bea.gov/news/schedule | read_html failed: `Import lxml` failed.  Use pip or conda to install the lxml package. |
| bls_cpi_release_schedule | reachable_not_parsed | 0 | https://www.bls.gov/schedule/news_release/cpi.htm | BLS CPI release schedule was reachable, but this pipeline has not found a stable parser/output format yet. No rows were stored. |
| bls_employment_release_schedule | reachable_not_parsed | 0 | https://www.bls.gov/schedule/news_release/empsit.htm | BLS employment release schedule was reachable, but this pipeline has not found a stable parser/output format yet. No rows were stored. |
| mops_shareholder_meeting_calendar | pending_endpoint_verification | 0 | https://mops.twse.com.tw/mops/web/t108sb19_q1 | MOPS shareholder meeting calendar exists on the website, but this pipeline has not confirmed a stable machine-readable endpoint yet. |

## What Is Already Stored

- TWSE ex-right/ex-dividend calendar is stored when the official endpoint returns rows.
- Monthly revenue expected windows are generated from Taiwan reporting rules for tracked stocks.
- FOMC and BEA macro dates are stored when official pages are reachable.

## Pending Sources

- Shareholder meeting dates need a stable MOPS endpoint before automated storage.
- BLS CPI/employment schedules may be blocked from this environment; keep them pending until a reliable official endpoint is found.
- Company-specific technology validation, exhibitions, law conferences, and news catalysts need explicit source rows in event_catalyst_log.csv before they can affect stock ranking.
