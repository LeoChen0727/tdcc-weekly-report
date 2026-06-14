# Calendar Data Source Status

- generated_at: `2026-06-15 03:58:24 Asia/Taipei`
- policy: Official/known-calendar sources are stored. Missing or blocked sources remain pending instead of being fabricated.

| source | status | rows | url | note |
|---|---|---:|---|---|
| twse_ex_right_ex_dividend | ok | 276 | https://www.twse.com.tw/rwd/zh/exRight/TWT48U?response=json |  |
| twse_shareholder_meeting_from_dividend_distribution | failed | 0 | https://openapi.twse.com.tw/v1/opendata/t187ap45_L | HTTPSConnectionPool(host='openapi.twse.com.tw', port=443): Max retries exceeded with url: /v1/opendata/t187ap45_L (Caused by ConnectTimeoutError(<HTTPSConnection(host='openapi.twse.com.tw', port=443) at 0x7f1d2dd7b550>, 'Connection to openapi.twse.com.tw timed out. (connect timeout=30)')) |
| monthly_revenue_expected_window | rule_based_expected_window | 313 | https://mops.twse.com.tw/mops/web/t05st10_ifrs | Expected monthly revenue publication window generated for tracked stocks; not a confirmed company catalyst. |
| federal_reserve_fomc | ok | 13 | https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm |  |
| bea_release_schedule | ok | 22 | https://www.bea.gov/news/schedule |  |
| bls_cpi_release_schedule | ok | 7 | https://www.bls.gov/schedule/news_release/cpi.htm | Parsed 7 release rows from the official BLS schedule table. |
| bls_employment_release_schedule | ok | 6 | https://www.bls.gov/schedule/news_release/empsit.htm | Parsed 6 release rows from the official BLS schedule table. |
| mops_shareholder_meeting_calendar | blocked_or_unavailable | 0 | https://mops.twse.com.tw/mops/web/t108sb31new | TWSE-listed shareholder meeting dates are stored from t187ap45_L. Direct MOPS shareholder pages are blocked or unavailable from this environment, and OTC coverage still needs a stable official endpoint. |

## What Is Already Stored

- TWSE ex-right/ex-dividend calendar is stored when the official endpoint returns rows.
- Monthly revenue expected windows are generated from Taiwan reporting rules for tracked stocks.
- FOMC and BEA macro dates are stored when official pages are reachable.

## Pending Sources

- TWSE shareholder meeting dates are stored from official OpenAPI where available; MOPS/TPEX coverage remains pending if blocked.
- BLS CPI/employment schedules are stored when official schedule tables are reachable and parseable.
- Company-specific technology validation, exhibitions, law conferences, and news catalysts need explicit source rows in event_catalyst_log.csv before they can affect stock ranking.
