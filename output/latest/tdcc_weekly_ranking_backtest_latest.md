# TDCC Weekly Ranking Formula Backtest

- model_id: `tdcc_weekly_ranking_formula`
- ranking_model_version: `tdcc_weekly_ranking_formula_20260614`
- generated_at: `2026-06-30 22:19:55 Asia/Taipei`
- event_rows: `880`
- scope: research only; this does not generate TDCC weekly PDFs and does not approve production buy signals.
- theme_context: latest taxonomy is used for the +5 mainstream bonus; treat that as a first-pass research limitation.

## Top Summary

| tdcc_list_type | rank_bucket | horizon | event_count | win_rate | avg_return | median_return | out_of_sample_size | out_of_sample_pass | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_20 | D+20 | 68 | 52.94 | 9.5865 | 1.1372 | 60 | True | medium |
| consecutive_accumulation | top_10 | D+20 | 38 | 47.37 | 6.8818 | -1.0173 | 30 | True | low |
| consecutive_accumulation | top_50 | D+20 | 112 | 49.11 | 6.866 | -1.0173 | 104 | True | medium |
| weekly_increase | top_50 | D+20 | 451 | 49.0 | 6.0499 | 0.0 | 210 | True | high |
| weekly_increase | top_20 | D+20 | 331 | 46.22 | 5.0106 | -0.4886 | 90 | True | high |
| weekly_increase | top_10 | D+20 | 232 | 46.12 | 4.4216 | -0.5484 | 49 | True | high |
| consecutive_accumulation | top_50 | D+10 | 184 | 51.63 | 3.7627 | 0.2967 | 176 | True | high |
| weekly_increase | top_50 | D+10 | 551 | 50.27 | 3.7382 | 0.1567 | 310 | True | high |
| consecutive_accumulation | top_20 | D+10 | 108 | 51.85 | 3.4347 | 0.567 | 100 | True | medium |
| weekly_increase | top_20 | D+10 | 371 | 48.79 | 2.8156 | -0.2398 | 130 | True | high |
| weekly_increase | top_10 | D+10 | 252 | 49.6 | 2.706 | 0.0 | 69 | True | high |
| consecutive_accumulation | top_10 | D+10 | 58 | 44.83 | 2.1794 | -1.6393 | 50 | False | medium |
| weekly_increase | top_50 | D+5 | 601 | 45.26 | 1.6474 | -0.4706 | 360 | False | high |
| consecutive_accumulation | top_20 | D+5 | 124 | 47.58 | 1.6011 | -0.552 | 116 | False | high |
| consecutive_accumulation | top_10 | D+5 | 68 | 38.24 | 1.5126 | -3.4153 | 60 | False | medium |
| consecutive_accumulation | top_50 | D+5 | 200 | 49.5 | 1.4631 | 0.0 | 192 | True | high |
| weekly_increase | top_10 | D+5 | 262 | 44.66 | 1.3701 | -0.406 | 79 | True | high |
| weekly_increase | top_20 | D+5 | 391 | 46.29 | 1.3581 | -0.2506 | 150 | True | high |

## Promotion Guardrail

- `approved_for_daily` is always `False`.
- A future promotion needs explicit approval, out-of-sample pass, sufficient samples, and a production PR.