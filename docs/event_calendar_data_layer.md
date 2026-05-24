# Event Calendar Data Layer

This layer stores known or expected calendar events before the daily candidate report is generated.

## Stored Tables

- `data/company_calendar/company_event_calendar.csv`: stock-level events such as TWSE ex-dividend/ex-right dates and monthly revenue expected windows.
- `data/macro_events/macro_event_calendar.csv`: macro events used by the market-risk dashboard, such as FOMC and BEA releases.
- `output/latest/upcoming_catalyst_calendar_latest.csv`: nearby stock-level events for candidate tagging.
- `output/latest/upcoming_macro_event_calendar_latest.csv`: nearby macro events for the market-risk report.
- `output/latest/calendar_data_source_status_latest.md`: source status and blocked/pending sources.

## Current Sources

- TWSE ex-right/ex-dividend calendar: official endpoint, stored when reachable.
- Monthly revenue expected window: rule-based Taiwan reporting calendar reminder, not a confirmed company catalyst.
- Federal Reserve FOMC calendar: official page, parsed when reachable.
- BEA release schedule: official page, parsed when reachable.

## Pending Sources

- MOPS shareholder meeting dates need a stable machine-readable endpoint before automation.
- BLS CPI/employment schedules may block automated access from GitHub Actions or local requests; blocked sources are recorded in the status file.
- Company-specific technology validation, exhibitions, legal conferences, and news catalysts require source rows in `data/event_catalysts/event_catalyst_log.csv`.

## Model Rule

Calendar proximity is a reminder layer. It can add `event_calendar_tags`, `nearest_event_date`, and `event_proximity_score`, but it does not upgrade a stock by itself. A stock still needs confirmed financial/event evidence, low price reaction, and non-weak TDCC/price behavior before it can be treated as a stronger catalyst candidate.
