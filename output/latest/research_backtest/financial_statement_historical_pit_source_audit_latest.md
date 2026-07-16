# Historical Financial Statement PIT Source Audit

- audit_id: `financial_statement_historical_pit_source_audit_v1`
- conclusion: `blocked_exact_initial_filed_at_and_complete_revision_payload_history_unavailable`
- target coverage: `2013Q1 onward`
- current tracked price-history overlap: `2025-04-07 onward` (verified for the cross-market and cross-industry pilot stocks at source-audit time)
- `pit_eligible=False`
- `formal_model_use_allowed=False`

The official MOPS bulk and single-company XBRL surfaces provide period payloads, report scope, industry taxonomy, and correction-event evidence. They do not provide a reproducible initial company filing timestamp plus every before/after revision payload. ZIP member times are archive rebuild times, and `ReviewAuditDate` is not MOPS filing availability.
The 2013Q1 archive is an earliest-IFRS source-contract probe, not current backtest evidence. The 2025Q1 archive is the first pilot quarter near the current tracked price-history window. Financial-statement source retention and research-price overlap are separate gates.

| Period | Archive SHA-256 | Members | Scope evidence | Taxonomy evidence | Result |
| --- | --- | ---: | --- | --- | --- |
| 2013Q1 | `f6974e00aec749a3486d7944871fbe299129bdfe4107f1f4453699272b266f16` | 1530 | cr=1381;ir=149;t163sb01 labels 2330 listed and 5347 OTC while the XBRL identifier scheme itself does not distinguish markets | tifrs-ci-cr-2013-03-31.xsd;tifrs-fh-2013-03-31.xsd;tifrs-ins-ir-2013-03-31.xsd | `pilot_payload_and_scope_verified_pit_blocked` |
| 2025Q1 | `975c3439879d92bb336476f0691cc0547108b19603d06940439963c5fba1cb11` | 1986 | cr=1804;ir=182;t163sb01 labels 2330 listed and 5347 OTC while the XBRL identifier scheme itself does not distinguish markets | tifrs-ci-cr-2020-06-30.xsd;tifrs-fh-2020-06-30.xsd;tifrs-ins-ir-2020-06-30.xsd | `pilot_payload_and_scope_verified_pit_blocked` |

## Formal-use boundary

Until an official reproducible source supplies exact initial filing availability and complete revision payload lineage, EPS, gross margin, operating margin, operating income, non-operating income, and net income must not enter `revenue_unreacted_range`, any production gate, score, ranking, PDF, packet, or promotion evidence.

The next admissible implementation is a source adapter that can bind each company-period-scope revision to an immutable payload SHA-256 and an official availability timestamp or date. Statutory deadlines, audit/review dates, ZIP timestamps, and first-observed local capture times are not substitutes.
