# Daily PDF Completion Hard Gate

This document records the daily PDF completion gate added for model and PDF
maintenance work.

The enforcing validator is `scripts/validate_daily_pdf_completion_hard_gate.py`.

The gate is intentionally a completion check, not a layout or model rule. It
does not choose stocks, score models, rank rows, infer lifecycle rows, or change
PDF visual design.

The enforced requirements are:

- Daily PDF and model-maintenance PR workflows must run the PDF contract,
  role-manifest, shared-path, production-inventory, and completion hard-gate
  validators.
- A PR or main run that replays ChatGPT-side daily PDFs must validate the replay
  output directory after rendering.
- The replay output directory must contain exactly the six manifest-listed PDFs.
- `chatgpt_daily_report_runtime_manifest.json` must exist and provide the
  machine-readable PDF role map.
- `chatgpt_daily_pdf_semantic_manifest.csv` must exist and be referenced by
  the runtime manifest. It records machine-readable operation row semantics
  (`pdf_role`, `model_id`, `pdf_section`, `stock_id`, `source_artifact`, and
  `source_sha256`) so PDF row placement is validated without relying only on
  extracted text.
- The six PDFs must open, expose extractable text, and pass rendered model text
  regression.
- The semantic manifest must pass schema checks, forbidden legacy/preview source
  checks, and configured golden semantic cases such as the 2026-07-06 accident
  guard rows.
- PDF-integrated operation models must have readiness status
  `pdf_integrated_daily_adapter`, `presentation_allowed=True`, model-owned
  adapter artifacts, required adapter sections, required PDF-safe columns, and
  renderer-consumption tokens.

This gate exists to prevent a PR from being treated as complete when code was
merged but the PDFs were not generated, not inspected by validation, or not
connected to the formal model-owned operation adapter.
