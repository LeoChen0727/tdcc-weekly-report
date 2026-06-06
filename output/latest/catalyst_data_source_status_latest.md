# Catalyst Data Source Status

- generated_at: `2026-06-06 11:19:06 Asia/Taipei`
- external_fetch_status: `not_configured`
- note: Schema and local/manual data tables are prepared. No unverified news, MOPS, or social rumor data is fabricated.

| data_table | path | rows |
|---|---|---:|
| theme_event_calendar | `data/theme_events/theme_event_calendar.csv` | 1 |
| company_theme_mapping | `data/theme_events/company_theme_mapping.csv` | 28 |
| quarterly_catalyst | `data/fundamental_catalysts/quarterly_catalyst.csv` | 0 |
| event_catalyst_log | `data/event_catalysts/event_catalyst_log.csv` | 0 |

## Data Policy

- Company announcements, MOPS, official financial statements, official exhibition pages, and company releases should be loaded into these tables before being treated as confirmed catalysts.
- Empty rows mean the catalyst is not available yet. The daily model keeps fields blank instead of inventing a catalyst.
