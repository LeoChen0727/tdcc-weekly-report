# Event Calendar Data Layer

This layer stores known or expected calendar events before the daily candidate report is generated.

## Stored Tables

- `data/company_calendar/company_event_calendar.csv`: stock-level events such as TWSE ex-dividend/ex-right dates and monthly revenue expected windows.
- `data/macro_events/macro_event_calendar.csv`: macro events used by the market-risk dashboard, such as FOMC and BEA releases.
- `output/latest/upcoming_catalyst_calendar_latest.csv`: nearby stock-level events for candidate tagging.
- `output/latest/upcoming_macro_event_calendar_latest.csv`: nearby macro events for the market-risk report.
- `output/latest/calendar_data_source_status_latest.md`: source status and blocked/pending sources.
- `output/latest/catalyst_needs_review_latest.csv`: pending or blocked catalyst sources that are not allowed to affect scoring.
- `output/latest/catalyst_needs_review_latest.md`: readable review list for unresolved data-source work.

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

Rows in `catalyst_needs_review_latest.csv` are blocked from model and PDF effects. `model_effect_allowed=False` means the row cannot affect score, rank, upgrade, downgrade, or `similar_to_shihsinko_flag`. `pdf_effect_allowed=False` means the row cannot be used as a formal recommendation reason in generated PDFs.

## Report Source Priority

ChatGPT and downstream report readers should use original structured data first: packet fields, CSV/raw URLs, signal logs, warrant tables, market tables, catalyst source logs, and validation files. PDF files are auxiliary/shareable outputs. If raw/source tables cannot be read and only PDF content is used, the report must disclose that at the beginning.
