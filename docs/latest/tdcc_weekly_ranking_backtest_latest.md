# TDCC Weekly Ranking Formula Backtest

- model_id: `tdcc_weekly_ranking_formula`
- ranking_model_version: `tdcc_weekly_ranking_formula_20260614`
- source_tdcc_dataset_id: `tdcc-20260717-98c564c5bc4ab725`
- generated_at: `2026-07-19 10:49:47 Asia/Taipei`
- event_rows: `1079`
- scope: research only; this does not generate TDCC weekly PDFs and does not approve production buy signals.
- theme_context: latest taxonomy is used for the +5 mainstream bonus; treat that as a first-pass research limitation.

## Top Summary

| tdcc_list_type | rank_bucket | horizon | event_count | win_rate | avg_return | median_return | out_of_sample_size | out_of_sample_pass | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| weekly_increase | top_50 | D+20 | 550 | 45.27 | 4.429 | -0.8226 | 249 | False | high |
| weekly_increase | top_20 | D+20 | 370 | 45.14 | 4.1792 | -0.754 | 99 | False | high |
| weekly_increase | top_10 | D+20 | 252 | 46.43 | 4.1591 | -0.4787 | 50 | True | high |
| consecutive_accumulation | top_50 | D+10 | 228 | 51.75 | 3.3557 | 0.3966 | 220 | True | high |
| consecutive_accumulation | top_20 | D+20 | 108 | 39.81 | 3.3545 | -3.2428 | 100 | False | medium |
| weekly_increase | top_50 | D+10 | 651 | 49.46 | 3.1789 | 0.0 | 350 | True | high |
| consecutive_accumulation | top_50 | D+20 | 184 | 41.85 | 3.1464 | -2.9959 | 176 | False | high |
| consecutive_accumulation | top_20 | D+10 | 144 | 50.69 | 2.7678 | 0.1458 | 136 | True | high |
| weekly_increase | top_20 | D+10 | 411 | 48.18 | 2.5726 | -0.3155 | 140 | True | high |
| weekly_increase | top_10 | D+10 | 272 | 49.26 | 2.4683 | -0.0806 | 70 | True | high |
| consecutive_accumulation | top_10 | D+10 | 78 | 46.15 | 2.2478 | -1.4278 | 70 | False | medium |
| consecutive_accumulation | top_10 | D+20 | 58 | 37.93 | 1.8926 | -4.4656 | 50 | False | medium |
| weekly_increase | top_20 | D+5 | 451 | 45.68 | 0.9051 | -0.381 | 180 | False | high |
| weekly_increase | top_50 | D+5 | 751 | 43.81 | 0.8769 | -0.7353 | 450 | False | high |
| weekly_increase | top_10 | D+5 | 292 | 44.52 | 0.722 | -0.465 | 90 | False | high |
| consecutive_accumulation | top_50 | D+5 | 264 | 47.35 | 0.6573 | -0.4079 | 256 | False | high |
| consecutive_accumulation | top_20 | D+5 | 180 | 44.44 | 0.2674 | -2.1883 | 172 | False | high |
| consecutive_accumulation | top_10 | D+5 | 98 | 36.73 | -0.1331 | -3.6221 | 90 | False | medium |

## Promotion Guardrail

- `approved_for_daily` is always `False`.
- A future promotion needs explicit approval, out-of-sample pass, sufficient samples, and a production PR.