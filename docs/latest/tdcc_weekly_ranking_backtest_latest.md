# TDCC Weekly Ranking Formula Backtest

- model_id: `tdcc_weekly_ranking_formula`
- ranking_model_version: `tdcc_weekly_ranking_formula_20260614`
- generated_at: `2026-06-21 20:41:44 Asia/Taipei`
- event_rows: `802`
- scope: research only; this does not generate TDCC weekly PDFs and does not approve production buy signals.
- theme_context: latest taxonomy is used for the +5 mainstream bonus; treat that as a first-pass research limitation.

## Top Summary

| tdcc_list_type | rank_bucket | horizon | event_count | win_rate | avg_return | median_return | out_of_sample_size | out_of_sample_pass | confidence_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| consecutive_accumulation | top_20 | D+20 | 28 | 60.71 | 12.5286 | 3.4616 | 20 | True | low |
| consecutive_accumulation | top_50 | D+20 | 36 | 63.89 | 12.3028 | 5.8641 | 28 | True | low |
| consecutive_accumulation | top_10 | D+20 | 18 | 50.0 | 10.7441 | 0.2838 | 10 | False | low |
| consecutive_accumulation | top_20 | D+10 | 68 | 57.35 | 6.5138 | 3.3555 | 60 | True | medium |
| weekly_increase | top_50 | D+20 | 350 | 48.29 | 4.9425 | -0.2273 | 127 | True | high |
| consecutive_accumulation | top_50 | D+10 | 113 | 54.87 | 4.7749 | 1.3423 | 105 | True | medium |
| consecutive_accumulation | top_10 | D+10 | 38 | 47.37 | 4.2467 | -1.6393 | 30 | True | low |
| weekly_increase | top_50 | D+10 | 451 | 50.78 | 4.0476 | 0.2924 | 228 | True | high |
| weekly_increase | top_20 | D+20 | 291 | 45.36 | 3.6916 | -0.6329 | 68 | True | high |
| weekly_increase | top_10 | D+20 | 212 | 45.28 | 3.2633 | -0.6206 | 39 | True | high |
| weekly_increase | top_20 | D+10 | 331 | 47.73 | 2.8806 | -0.346 | 108 | True | high |
| weekly_increase | top_10 | D+10 | 232 | 47.84 | 2.4296 | -0.4163 | 59 | True | high |
| consecutive_accumulation | top_20 | D+5 | 88 | 48.86 | 2.1714 | -0.4161 | 80 | True | medium |
| weekly_increase | top_50 | D+5 | 501 | 46.51 | 1.6223 | -0.2639 | 278 | True | high |
| consecutive_accumulation | top_50 | D+5 | 158 | 49.37 | 1.4981 | 0.0 | 150 | True | high |
| consecutive_accumulation | top_10 | D+5 | 48 | 39.58 | 1.2852 | -2.964 | 40 | False | low |
| weekly_increase | top_20 | D+5 | 351 | 46.72 | 1.1546 | -0.2183 | 128 | True | high |
| weekly_increase | top_10 | D+5 | 242 | 44.63 | 1.085 | -0.3723 | 69 | True | high |

## Promotion Guardrail

- `approved_for_daily` is always `False`.
- A future promotion needs explicit approval, out-of-sample pass, sufficient samples, and a production PR.