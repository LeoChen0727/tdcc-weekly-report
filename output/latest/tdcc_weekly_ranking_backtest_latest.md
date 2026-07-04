# TDCC Weekly Ranking Formula Backtest

- model_id: `tdcc_weekly_ranking_formula`
- ranking_model_version: `tdcc_weekly_ranking_formula_20260614`
- generated_at: `2026-07-05 04:09:52 Asia/Taipei`
- event_rows: `949`
- scope: research only; this does not generate TDCC weekly PDFs and does not approve production buy signals.
- theme_context: latest taxonomy is used for the +5 mainstream bonus; treat that as a first-pass research limitation.

## Top Summary

| tdcc_list_type | rank_bucket | horizon | event_count | win_rate | avg_return | median_return | out_of_sample_size | out_of_sample_pass | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_20 | D+20 | 68 | 52.94 | 9.5865 | 1.1372 | 60 | True | medium |
| consecutive_accumulation | top_10 | D+20 | 38 | 47.37 | 6.8818 | -1.0173 | 30 | True | low |
| consecutive_accumulation | top_50 | D+20 | 113 | 48.67 | 6.8026 | -0.8039 | 105 | True | medium |
| weekly_increase | top_50 | D+20 | 451 | 49.0 | 6.0499 | 0.0 | 210 | True | high |
| weekly_increase | top_20 | D+20 | 331 | 46.22 | 5.0106 | -0.4886 | 90 | True | high |
| weekly_increase | top_10 | D+20 | 232 | 46.12 | 4.4216 | -0.5484 | 49 | True | high |
| consecutive_accumulation | top_50 | D+10 | 200 | 51.5 | 3.706 | 0.2566 | 192 | True | high |
| weekly_increase | top_50 | D+10 | 601 | 49.92 | 3.4813 | 0.0 | 360 | True | high |
| consecutive_accumulation | top_20 | D+10 | 124 | 51.61 | 3.3856 | 0.2566 | 116 | True | high |
| consecutive_accumulation | top_10 | D+10 | 68 | 44.12 | 2.7684 | -1.6393 | 60 | False | medium |
| weekly_increase | top_20 | D+10 | 391 | 48.59 | 2.726 | -0.2398 | 150 | True | high |
| weekly_increase | top_10 | D+10 | 262 | 49.62 | 2.6113 | 0.0 | 79 | True | high |
| consecutive_accumulation | top_20 | D+5 | 144 | 51.39 | 2.2483 | 0.2191 | 136 | True | high |
| consecutive_accumulation | top_10 | D+5 | 78 | 42.31 | 2.1574 | -2.687 | 70 | False | medium |
| weekly_increase | top_50 | D+5 | 651 | 47.62 | 2.0299 | -0.221 | 410 | True | high |
| consecutive_accumulation | top_50 | D+5 | 228 | 52.19 | 1.9699 | 0.3597 | 220 | True | high |
| weekly_increase | top_20 | D+5 | 411 | 47.45 | 1.5877 | -0.2008 | 170 | True | high |
| weekly_increase | top_10 | D+5 | 272 | 45.96 | 1.5074 | -0.3195 | 89 | True | high |

## Promotion Guardrail

- `approved_for_daily` is always `False`.
- A future promotion needs explicit approval, out-of-sample pass, sufficient samples, and a production PR.