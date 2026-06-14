# AGENTS.md

精確.按照規則辦事

## Default Engineering Rule

All business-facing code in this repository defaults to independent ownership.

Do not share business-semantic code across unrelated reports, models, parameters,
ranking rules, filters, PDF layouts, packets, validations, workflows, or output
contracts unless the coupling is explicitly documented in repo rules and the
user has approved it.

Shared code is allowed only for low-level technical utilities that do not decide
business content, such as file reads, type conversion, date formatting, font
registration, basic table drawing, PDF file writing, and generic validation
plumbing.

Before editing any shared function, parameter table, helper, or workflow step,
first identify which reports, models, outputs, and validations depend on it. If
the requested change is for one surface, split the shared code path before
changing behavior.

Stock model parameters, thresholds, scoring weights, ranking rules, and gates
must be independent by default. They may be shared only when the same backtest
evidence explicitly proves that the models should share the parameter, and that
relationship is encoded in source rules and tests.

Changing A must not silently change B. If A and B are intentionally coupled,
state that coupling before making the change.

This is a repository-level engineering gate, not a style preference. Daily
production validation must run `scripts/validate_repo_code_isolation_policy.py`
and `scripts/validate_chatgpt_side_pdf_layout_independence.py`; weakening these
guards requires changing the validator and tests in the same reviewed PR.

