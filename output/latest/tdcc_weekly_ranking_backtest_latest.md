# TDCC Weekly Ranking Formula Backtest

- model_id: `tdcc_weekly_ranking_formula`
- ranking_model_version: `tdcc_weekly_ranking_formula_20260614`
- generated_at: `2026-06-14 20:50:23 Asia/Taipei`
- event_rows: `736`
- scope: research only; this does not generate TDCC weekly PDFs and does not approve production buy signals.
- theme_context: latest taxonomy is used for the +5 mainstream bonus; treat that as a first-pass research limitation.

## Top Summary

| tdcc_list_type | rank_bucket | horizon | event_count | win_rate | avg_return | median_return | out_of_sample_size | out_of_sample_pass | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_20 | D+10 | 48 | 68.75 | 11.5183 | 7.7538 | 40 | True | low |
| consecutive_accumulation | top_50 | D+10 | 64 | 68.75 | 10.0283 | 6.7662 | 56 | True | medium |
| consecutive_accumulation | top_10 | D+10 | 28 | 57.14 | 9.3933 | 3.0006 | 20 | True | low |
| weekly_increase | top_50 | D+10 | 401 | 53.37 | 4.8917 | 0.9677 | 196 | True | high |
| consecutive_accumulation | top_20 | D+5 | 68 | 55.88 | 4.1905 | 2.4472 | 60 | True | medium |
| weekly_increase | top_50 | D+20 | 300 | 46.67 | 3.7432 | -0.425 | 95 | True | high |
| consecutive_accumulation | top_50 | D+5 | 113 | 55.75 | 3.7201 | 1.5723 | 105 | True | medium |
| weekly_increase | top_20 | D+10 | 311 | 48.87 | 3.3591 | -0.1613 | 106 | True | high |
| weekly_increase | top_20 | D+20 | 271 | 44.65 | 2.9732 | -0.6356 | 66 | True | high |
| weekly_increase | top_10 | D+10 | 222 | 48.2 | 2.5988 | -0.2929 | 59 | True | high |
| consecutive_accumulation | top_10 | D+5 | 38 | 42.11 | 2.5484 | -1.8429 | 30 | False | low |
| weekly_increase | top_10 | D+20 | 202 | 44.06 | 2.3669 | -0.7197 | 39 | True | high |
| weekly_increase | top_50 | D+5 | 451 | 49.0 | 2.2765 | 0.0 | 246 | True | high |
| weekly_increase | top_20 | D+5 | 331 | 47.43 | 1.4882 | 0.0 | 126 | True | high |
| weekly_increase | top_10 | D+5 | 232 | 45.26 | 1.2667 | -0.3195 | 69 | True | high |
| consecutive_accumulation | top_10 | D+20 | 8 | 12.5 | -10.1503 | -12.7863 | 0 | False | low |
| consecutive_accumulation | top_20 | D+20 | 8 | 12.5 | -10.1503 | -12.7863 | 0 | False | low |
| consecutive_accumulation | top_50 | D+20 | 8 | 12.5 | -10.1503 | -12.7863 | 0 | False | low |

## Promotion Guardrail

- `approved_for_daily` is always `False`.
- A future promotion needs explicit approval, out-of-sample pass, sufficient samples, and a production PR.