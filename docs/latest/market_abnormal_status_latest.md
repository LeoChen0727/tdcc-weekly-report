# Market Abnormal Status Latest

- target_date: `20260826`
- fetch_date: `20260827`
- fetched_at: `2026-08-27 17:06:29 Asia/Taipei`
- access_mode: `historical_unavailable`
- raw_bundle_manifest: `data/market_abnormal_status/bundles/20260826/manifest.json`
- raw_bundle_manifest_sha256: `ee099a72f29d90d3dcb6703585ef0a7afa77413d2667380be1180838eb7511c8`
- intended_source: TWSE / TPEx official OpenAPI (not available for this target date)
- usage: execution-risk flag for daily candidate, short-term research, and backtest segmentation.
- limitation: legacy history rows with blank target_date predate exact-target bundle lineage and must not be used as point-in-time evidence.

## Availability

- status: `historical_unavailable`
- reason: `exact_target_raw_bundle_unavailable`
- interpretation: advisory execution-risk status was not checked; no stock may be inferred normal from this empty snapshot.

