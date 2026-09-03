# Catalyst Data Source Status

- generated_at: `2026-09-03 19:41:46 Asia/Taipei`
- external_fetch_status: `partial_ok`
- note: Official monthly revenue and material-information sources are used when reachable. No unverified news, MOPS pages, or social rumor data is fabricated.

| data_table | path | rows |
|---|---|---:|
| theme_event_calendar | `data/theme_events/theme_event_calendar.csv` | 1 |
| company_theme_mapping | `data/theme_events/company_theme_mapping.csv` | 28 |
| quarterly_catalyst | `data/fundamental_catalysts/quarterly_catalyst.csv` | 2434 |
| event_catalyst_log | `data/event_catalysts/event_catalyst_log.csv` | 3180 |

## External Source Status

| source | status | rows | matched_tracked_rows | url | note |
|---|---|---:|---:|---|---|
| TWSE monthly revenue OpenAPI | ok | 1085 | 256 | https://openapi.twse.com.tw/v1/opendata/t187ap05_L | Official monthly revenue rows are stored as fundamental source rows with EPS/margin fields blank. They can flag revenue_good_eps_unconfirmed only; they are not EPS confirmation. |
| TPEX monthly revenue OpenAPI | ok | 890 | 93 | https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O | Official monthly revenue rows are stored as fundamental source rows with EPS/margin fields blank. They can flag revenue_good_eps_unconfirmed only; they are not EPS confirmation. |
| TWSE material information OpenAPI | ok | 86 | 35 | https://openapi.twse.com.tw/v1/opendata/t187ap04_L | Official material-information rows are filtered to tracked stocks. Only objective order/customer/capacity/production/certification keywords become evidence event types; other rows stay material_information context. |
| TPEX material information OpenAPI | ok | 55 | 12 | https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap04_O | Official material-information rows are filtered to tracked stocks. Only objective order/customer/capacity/production/certification keywords become evidence event types; other rows stay material_information context. |

## Data Policy

- Company announcements, MOPS, official financial statements, official exhibition pages, and company releases should be loaded into these tables before being treated as confirmed catalysts.
- Empty rows mean the catalyst is not available yet. The daily model keeps fields blank instead of inventing a catalyst.
