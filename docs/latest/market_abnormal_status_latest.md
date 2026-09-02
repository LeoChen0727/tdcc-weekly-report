# Market Abnormal Status Latest

- target_date: `20260902`
- fetch_date: `20260903`
- fetched_at: `2026-09-03 02:34:55 Asia/Taipei`
- access_mode: `historical_unavailable`
- raw_bundle_manifest: `data/market_abnormal_status/bundles/20260902/manifest.json`
- raw_bundle_manifest_sha256: `cb0d0f3769f9a77de52151e01e9d7dd4bed1105c2543f0076c529904165f872d`
- intended_source: TWSE / TPEx official OpenAPI (not available for this target date)
- usage: execution-risk flag for daily candidate, short-term research, and backtest segmentation.
- limitation: legacy history rows with blank target_date predate exact-target bundle lineage and must not be used as point-in-time evidence.

## Availability

- status: `historical_unavailable`
- reason: `exact_target_raw_bundle_unavailable`
- interpretation: advisory execution-risk status was not checked; no stock may be inferred normal from this empty snapshot.

